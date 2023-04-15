from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    num_pools = models.PositiveIntegerField()
    num_teams_per_pool = models.PositiveIntegerField()

class Pool(models.Model):
    number = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='pools')

class Team(models.Model):
    name = models.CharField(max_length=255)
    coach_name = models.CharField(max_length=255)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name='teams')

class Match(models.Model):
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.PositiveIntegerField(null=True, blank=True)
    away_score = models.PositiveIntegerField(null=True, blank=True)

class Player(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
