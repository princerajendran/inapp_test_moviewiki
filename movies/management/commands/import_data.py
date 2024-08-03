from django.core.management.base import BaseCommand
import pandas as pd
from movies.models import Person, Title
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Import data from TSV files into Django models'

    def handle(self, *args, **kwargs):
        BATCH_SIZE = 1000
        DATA_PATH_PERSON = 'name.basics.tsv'
        DATA_PATH_TITLE = 'title.basics.tsv'

        person_df = pd.read_csv(DATA_PATH_PERSON, sep='\t', na_values='\\N')
        title_df = pd.read_csv(DATA_PATH_TITLE, sep='\t', na_values='\\N')

        def import_titles(df):
            title_objects = []
            for _, row in df.iterrows():
                title_objects.append(Title(
                    tconst=row['tconst'],
                    title_type=row['titleType'],
                    primary_title=row['primaryTitle'],
                    original_title=row['originalTitle'],
                    is_adult=bool(int(row['isAdult'])),
                    start_year=row['startYear'] if row['startYear'] != '\\N' else None,
                    end_year=row['endYear'] if row['endYear'] != '\\N' else None,
                    runtime_minutes=row['runtimeMinutes'] if row['runtimeMinutes'] != '\\N' else None,
                    genres=row['genres']
                ))
            with transaction.atomic():
                Title.objects.bulk_create(title_objects)

        def import_persons(df):
            person_objects = []
            for _, row in df.iterrows():
                person_objects.append(Person(
                    nconst=row['nconst'],
                    primary_name=row['primaryName'],
                    birth_year=row['birthYear'] if row['birthYear'] != '\\N' else None,
                    death_year=row['deathYear'] if row['deathYear'] != '\\N' else None,
                    primary_profession=row['primaryProfession']
                ))

            with transaction.atomic():
                Person.objects.bulk_create(person_objects)

        def update_relationships(df):
            for _, row in df.iterrows():
                try:
                    person = Person.objects.get(nconst=row['nconst'])
                    if not pd.isna(row['knownForTitles']):
                        titles = Title.objects.filter(tconst__in=row['knownForTitles'].split(','))
                        person.known_for_titles.set(titles)
                        person.save()
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Person with nconst {row['nconst']} does not exist."))

        for start in range(0, len(title_df), BATCH_SIZE):
            end = min(start + BATCH_SIZE, len(title_df))
            batch = title_df[start:end]
            import_titles(batch)

        for start in range(0, len(person_df), BATCH_SIZE):
            end = min(start + BATCH_SIZE, len(person_df))
            batch = person_df[start:end]
            import_persons(batch)

        for start in range(0, len(person_df), BATCH_SIZE):
            end = min(start + BATCH_SIZE, len(person_df))
            batch = person_df[start:end]
            update_relationships(batch)

        self.stdout.write(self.style.SUCCESS("Data import completed."))
