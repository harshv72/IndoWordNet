# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TblAdjectiveAlsoSee(models.Model):
    synset_id = models.IntegerField()
    also_see_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_also_see'


class TblAdjectiveAntoAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_action_id = models.IntegerField(blank=True, null=True)
    anto_action_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_action'


class TblAdjectiveAntoAmount(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_amount_id = models.IntegerField(blank=True, null=True)
    anto_amount_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_amount'


class TblAdjectiveAntoColour(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_colour_id = models.IntegerField(blank=True, null=True)
    anto_colour_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_colour'


class TblAdjectiveAntoDirection(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_direction_id = models.IntegerField(blank=True, null=True)
    anto_direction_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_direction'


class TblAdjectiveAntoGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_gender_id = models.IntegerField(blank=True, null=True)
    anto_gender_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_gender'


class TblAdjectiveAntoManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_manner_id = models.IntegerField(blank=True, null=True)
    anto_manner_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_manner'


class TblAdjectiveAntoPersonality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_personality_id = models.IntegerField(blank=True, null=True)
    anto_personality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_personality'


class TblAdjectiveAntoPlace(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_place_id = models.IntegerField(blank=True, null=True)
    anto_place_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_place'


class TblAdjectiveAntoQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_quality_id = models.IntegerField(blank=True, null=True)
    anto_quality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_quality'


class TblAdjectiveAntoSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_size_id = models.IntegerField(blank=True, null=True)
    anto_size_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_size'


class TblAdjectiveAntoState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_state_id = models.IntegerField(blank=True, null=True)
    anto_state_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_state'


class TblAdjectiveAntoTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_time_id = models.IntegerField(blank=True, null=True)
    anto_time_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_anto_time'


class TblAdjectiveDerivedFrom(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    derived_from_id = models.IntegerField(blank=True, null=True)
    derived_from_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_derived_from'


class TblAdjectiveGradAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_action_id = models.IntegerField(blank=True, null=True)
    grad_action_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_action'


class TblAdjectiveGradColor(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_color_id = models.IntegerField(blank=True, null=True)
    grad_color_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_color'


class TblAdjectiveGradGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_gender_id = models.IntegerField(blank=True, null=True)
    grad_gender_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_gender'


class TblAdjectiveGradLight(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_light_id = models.IntegerField(blank=True, null=True)
    grad_light_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_light'


class TblAdjectiveGradManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_manner_id = models.IntegerField(blank=True, null=True)
    grad_manner_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_manner'


class TblAdjectiveGradQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_quality_id = models.IntegerField(blank=True, null=True)
    grad_quality_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_quality'


class TblAdjectiveGradSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_size_id = models.IntegerField(blank=True, null=True)
    grad_size_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_size'


class TblAdjectiveGradState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_state_id = models.IntegerField(blank=True, null=True)
    grad_state_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_state'


class TblAdjectiveGradTemperature(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_temperature_id = models.IntegerField(blank=True, null=True)
    grad_temperature_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_temperature'


class TblAdjectiveGradTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_time_id = models.IntegerField(blank=True, null=True)
    grad_time_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_grad_time'


class TblAdjectiveModifiesNoun(models.Model):
    synset_id = models.IntegerField()
    modifies_noun_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_modifies_noun'


class TblAdjectiveRelations(models.Model):
    synset_id = models.IntegerField()
    link_type = models.CharField(max_length=100)
    tbl_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_relations'


class TblAdjectiveSenseNum(models.Model):
    word = models.CharField(max_length=100)
    sense_num = models.IntegerField()
    synset_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_adjective_sense_num'


class TblAdjectiveSimilar(models.Model):
    synset_id = models.IntegerField()
    similar_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adjective_similar'


class TblAdverbAlsoSee(models.Model):
    synset_id = models.IntegerField()
    also_see_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_also_see'


class TblAdverbAntoAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_action_id = models.IntegerField(blank=True, null=True)
    anto_action_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_action'


class TblAdverbAntoAmount(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_amount_id = models.IntegerField(blank=True, null=True)
    anto_amount_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_amount'


class TblAdverbAntoColour(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_colour_id = models.IntegerField(blank=True, null=True)
    anto_colour_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_colour'


class TblAdverbAntoDirection(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_direction_id = models.IntegerField(blank=True, null=True)
    anto_direction_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_direction'


class TblAdverbAntoGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_gender_id = models.IntegerField(blank=True, null=True)
    anto_gender_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_gender'


class TblAdverbAntoManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_manner_id = models.IntegerField(blank=True, null=True)
    anto_manner_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_manner'


class TblAdverbAntoPersonality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_personality_id = models.IntegerField(blank=True, null=True)
    anto_personality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_personality'


class TblAdverbAntoPlace(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_place_id = models.IntegerField(blank=True, null=True)
    anto_place_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_place'


class TblAdverbAntoQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_quality_id = models.IntegerField(blank=True, null=True)
    anto_quality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_quality'


class TblAdverbAntoSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_size_id = models.IntegerField(blank=True, null=True)
    anto_size_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_size'


class TblAdverbAntoState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_state_id = models.IntegerField(blank=True, null=True)
    anto_state_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_state'


class TblAdverbAntoTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_time_id = models.IntegerField(blank=True, null=True)
    anto_time_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_anto_time'


class TblAdverbDerivedFrom(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    derived_from_id = models.IntegerField(blank=True, null=True)
    derived_from_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_derived_from'


class TblAdverbGradAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_action_id = models.IntegerField(blank=True, null=True)
    grad_action_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_action'


class TblAdverbGradColor(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_color_id = models.IntegerField(blank=True, null=True)
    grad_color_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_color'


class TblAdverbGradGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_gender_id = models.IntegerField(blank=True, null=True)
    grad_gender_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_gender'


class TblAdverbGradLight(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_light_id = models.IntegerField(blank=True, null=True)
    grad_light_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_light'


class TblAdverbGradManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_manner_id = models.IntegerField(blank=True, null=True)
    grad_manner_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_manner'


class TblAdverbGradQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_quality_id = models.IntegerField(blank=True, null=True)
    grad_quality_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_quality'


class TblAdverbGradSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_size_id = models.IntegerField(blank=True, null=True)
    grad_size_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_size'


class TblAdverbGradState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_state_id = models.IntegerField(blank=True, null=True)
    grad_state_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_state'


class TblAdverbGradTemperature(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_temperature_id = models.IntegerField(blank=True, null=True)
    grad_temperature_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_temperature'


class TblAdverbGradTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_time_id = models.IntegerField(blank=True, null=True)
    grad_time_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_grad_time'


class TblAdverbModifiesVerb(models.Model):
    synset_id = models.IntegerField()
    modifies_verb_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_modifies_verb'


class TblAdverbRelations(models.Model):
    synset_id = models.IntegerField()
    link_type = models.CharField(max_length=100)
    tbl_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adverb_relations'


class TblAdverbSenseNum(models.Model):
    word = models.CharField(max_length=100)
    sense_num = models.IntegerField()
    synset_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_adverb_sense_num'


class TblAllSynset(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.BinaryField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_synset'


class TblAllWords(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=100)
    pos = models.CharField(max_length=100)
    sense_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_all_words'


class TblMorphRules(models.Model):
    ending = models.CharField(max_length=20)
    suffix = models.CharField(max_length=20, blank=True, null=True)
    pos = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_morph_rules'


class TblNearSynset(models.Model):
    synset_id = models.IntegerField()
    near_synset_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_near_synset'


class TblNounAbilityVerb(models.Model):
    synset_id = models.IntegerField()
    ability_verb_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_ability_verb'


class TblNounAntoAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_action_id = models.IntegerField(blank=True, null=True)
    anto_action_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_action'


class TblNounAntoAmount(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_amount_id = models.IntegerField(blank=True, null=True)
    anto_amount_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_amount'


class TblNounAntoColour(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_colour_id = models.IntegerField(blank=True, null=True)
    anto_colour_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_colour'


class TblNounAntoDirection(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_direction_id = models.IntegerField(blank=True, null=True)
    anto_direction_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_direction'


class TblNounAntoGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_gender_id = models.IntegerField(blank=True, null=True)
    anto_gender_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_gender'


class TblNounAntoManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_manner_id = models.IntegerField(blank=True, null=True)
    anto_manner_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_manner'


class TblNounAntoPersonality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_personality_id = models.IntegerField(blank=True, null=True)
    anto_personality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_personality'


class TblNounAntoPlace(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_place_id = models.IntegerField(blank=True, null=True)
    anto_place_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_place'


class TblNounAntoQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_quality_id = models.IntegerField(blank=True, null=True)
    anto_quality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_quality'


class TblNounAntoSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_size_id = models.IntegerField(blank=True, null=True)
    anto_size_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_size'


class TblNounAntoState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_state_id = models.IntegerField(blank=True, null=True)
    anto_state_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_state'


class TblNounAntoTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_time_id = models.IntegerField(blank=True, null=True)
    anto_time_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_anto_time'


class TblNounAttributes(models.Model):
    synset_id = models.IntegerField()
    attributes_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_attributes'


class TblNounCapabilityVerb(models.Model):
    synset_id = models.IntegerField()
    capability_verb_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_capability_verb'


class TblNounCompound(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    compound_id = models.IntegerField(blank=True, null=True)
    compound_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_compound'


class TblNounDerivedFrom(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    derived_from_id = models.IntegerField(blank=True, null=True)
    derived_from_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_derived_from'


class TblNounFunctionVerb(models.Model):
    synset_id = models.IntegerField()
    function_verb_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_function_verb'


class TblNounGradAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_action_id = models.IntegerField(blank=True, null=True)
    grad_action_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_action'


class TblNounGradColor(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_color_id = models.IntegerField(blank=True, null=True)
    grad_color_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_color'


class TblNounGradGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_gender_id = models.IntegerField(blank=True, null=True)
    grad_gender_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_gender'


class TblNounGradLight(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_light_id = models.IntegerField(blank=True, null=True)
    grad_light_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_light'


class TblNounGradManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_manner_id = models.IntegerField(blank=True, null=True)
    grad_manner_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_manner'


class TblNounGradQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_quality_id = models.IntegerField(blank=True, null=True)
    grad_quality_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_quality'


class TblNounGradSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_size_id = models.IntegerField(blank=True, null=True)
    grad_size_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_size'


class TblNounGradState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_state_id = models.IntegerField(blank=True, null=True)
    grad_state_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_state'


class TblNounGradTemperature(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_temperature_id = models.IntegerField(blank=True, null=True)
    grad_temperature_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_temperature'


class TblNounGradTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_time_id = models.IntegerField(blank=True, null=True)
    grad_time_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_grad_time'


class TblNounHoloComponentObject(models.Model):
    synset_id = models.IntegerField()
    holo_component_object_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_component_object'


class TblNounHoloFeatureActivity(models.Model):
    synset_id = models.IntegerField()
    holo_feature_activity_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_feature_activity'


class TblNounHoloMemberCollection(models.Model):
    synset_id = models.IntegerField()
    holo_member_collection_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_member_collection'


class TblNounHoloPhaseState(models.Model):
    synset_id = models.IntegerField()
    holo_phase_state_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_phase_state'


class TblNounHoloPlaceArea(models.Model):
    synset_id = models.IntegerField()
    holo_place_area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_place_area'


class TblNounHoloPortionMass(models.Model):
    synset_id = models.IntegerField()
    holo_portion_mass_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_portion_mass'


class TblNounHoloPositionArea(models.Model):
    synset_id = models.IntegerField()
    holo_position_area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_position_area'


class TblNounHoloResourceProcess(models.Model):
    synset_id = models.IntegerField()
    holo_resource_process_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_resource_process'


class TblNounHoloStuffObject(models.Model):
    synset_id = models.IntegerField()
    holo_stuff_object_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_holo_stuff_object'


class TblNounHypernymy(models.Model):
    synset_id = models.IntegerField()
    hypernymy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_hypernymy'


class TblNounHyponymy(models.Model):
    synset_id = models.IntegerField()
    hyponymy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_hyponymy'


class TblNounMeroComponentObject(models.Model):
    synset_id = models.IntegerField()
    mero_component_object_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_component_object'


class TblNounMeroFeatureActivity(models.Model):
    synset_id = models.IntegerField()
    mero_feature_activity_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_feature_activity'


class TblNounMeroMemberCollection(models.Model):
    synset_id = models.IntegerField()
    mero_member_collection_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_member_collection'


class TblNounMeroPhaseState(models.Model):
    synset_id = models.IntegerField()
    mero_phase_state_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_phase_state'


class TblNounMeroPlaceArea(models.Model):
    synset_id = models.IntegerField()
    mero_place_area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_place_area'


class TblNounMeroPortionMass(models.Model):
    synset_id = models.IntegerField()
    mero_portion_mass_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_portion_mass'


class TblNounMeroPositionArea(models.Model):
    synset_id = models.IntegerField()
    mero_position_area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_position_area'


class TblNounMeroResourceProcess(models.Model):
    synset_id = models.IntegerField()
    mero_resource_process_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_resource_process'


class TblNounMeroStuffObject(models.Model):
    synset_id = models.IntegerField()
    mero_stuff_object_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_mero_stuff_object'


class TblNounRelations(models.Model):
    synset_id = models.IntegerField()
    link_type = models.CharField(max_length=100)
    tbl_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_noun_relations'


class TblNounSenseNum(models.Model):
    word = models.CharField(max_length=100)
    sense_num = models.IntegerField()
    synset_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_noun_sense_num'


class TblOntoData(models.Model):
    onto_id = models.IntegerField(primary_key=True)
    onto_data = models.CharField(max_length=250, blank=True, null=True)
    onto_desc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_onto_data'


class TblOntoMap(models.Model):
    parent_id = models.IntegerField(primary_key=True)
    child_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_onto_map'


class TblOntoNodes(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    onto_nodes_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_onto_nodes'


class TblRelationType(models.Model):
    tbl_name = models.CharField(max_length=100)
    rel_type = models.CharField(max_length=100)
    pos = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_relation_type'


class TblSenseCount(models.Model):
    word = models.CharField(max_length=100)
    sense_count = models.IntegerField(blank=True, null=True)
    pos = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sense_count'


class TblVerbAlsoSee(models.Model):
    synset_id = models.IntegerField()
    also_see_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_also_see'


class TblVerbAntoAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_action_id = models.IntegerField(blank=True, null=True)
    anto_action_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_action'


class TblVerbAntoAmount(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_amount_id = models.IntegerField(blank=True, null=True)
    anto_amount_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_amount'


class TblVerbAntoColour(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_colour_id = models.IntegerField(blank=True, null=True)
    anto_colour_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_colour'


class TblVerbAntoDirection(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_direction_id = models.IntegerField(blank=True, null=True)
    anto_direction_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_direction'


class TblVerbAntoGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_gender_id = models.IntegerField(blank=True, null=True)
    anto_gender_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_gender'


class TblVerbAntoManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_manner_id = models.IntegerField(blank=True, null=True)
    anto_manner_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_manner'


class TblVerbAntoPersonality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_personality_id = models.IntegerField(blank=True, null=True)
    anto_personality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_personality'


class TblVerbAntoPlace(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_place_id = models.IntegerField(blank=True, null=True)
    anto_place_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_place'


class TblVerbAntoQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_quality_id = models.IntegerField(blank=True, null=True)
    anto_quality_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_quality'


class TblVerbAntoSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_size_id = models.IntegerField(blank=True, null=True)
    anto_size_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_size'


class TblVerbAntoState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_state_id = models.IntegerField(blank=True, null=True)
    anto_state_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_state'


class TblVerbAntoTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    anto_time_id = models.IntegerField(blank=True, null=True)
    anto_time_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_anto_time'


class TblVerbCausative(models.Model):
    synset_id = models.IntegerField()
    causative_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_causative'


class TblVerbCompounding(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    compounding_id = models.IntegerField(blank=True, null=True)
    compounding_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_compounding'


class TblVerbConjunction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    conjunction_id = models.IntegerField(blank=True, null=True)
    conjunction_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_conjunction'


class TblVerbDerivedFrom(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    derived_from_id = models.IntegerField(blank=True, null=True)
    derived_from_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_derived_from'


class TblVerbEntailment(models.Model):
    synset_id = models.IntegerField()
    entailment_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_entailment'


class TblVerbGradAction(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_action_id = models.IntegerField(blank=True, null=True)
    grad_action_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_action'


class TblVerbGradColor(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_color_id = models.IntegerField(blank=True, null=True)
    grad_color_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_color'


class TblVerbGradGender(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_gender_id = models.IntegerField(blank=True, null=True)
    grad_gender_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_gender'


class TblVerbGradLight(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_light_id = models.IntegerField(blank=True, null=True)
    grad_light_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_light'


class TblVerbGradManner(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_manner_id = models.IntegerField(blank=True, null=True)
    grad_manner_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_manner'


class TblVerbGradQuality(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_quality_id = models.IntegerField(blank=True, null=True)
    grad_quality_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_quality'


class TblVerbGradSize(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_size_id = models.IntegerField(blank=True, null=True)
    grad_size_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_size'


class TblVerbGradState(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_state_id = models.IntegerField(blank=True, null=True)
    grad_state_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_state'


class TblVerbGradTemperature(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_temperature_id = models.IntegerField(blank=True, null=True)
    grad_temperature_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_temperature'


class TblVerbGradTime(models.Model):
    synset_id = models.IntegerField()
    synset_word = models.CharField(max_length=100, blank=True, null=True)
    grad_time_id = models.IntegerField(blank=True, null=True)
    grad_time_word = models.CharField(max_length=100, blank=True, null=True)
    mid_synset_id = models.IntegerField(blank=True, null=True)
    mid_word = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_grad_time'


class TblVerbHypernymy(models.Model):
    synset_id = models.IntegerField()
    hypernymy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_hypernymy'


class TblVerbRelations(models.Model):
    synset_id = models.IntegerField()
    link_type = models.CharField(max_length=100)
    tbl_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_relations'


class TblVerbSenseNum(models.Model):
    word = models.CharField(max_length=100)
    sense_num = models.IntegerField()
    synset_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_verb_sense_num'


class TblVerbTroponymy(models.Model):
    synset_id = models.IntegerField()
    troponymy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_verb_troponymy'

class EnglishHindiIdMapping(models.Model):
    hindi_id = models.IntegerField(primary_key=True)
    hindi_category = models.CharField(max_length=100, blank=True, null=True)
    english_id = models.IntegerField(blank=True, null=True)
    english_category = models.CharField(max_length=100, blank=True, null=True)
    type_link = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'english_hindi_id_mapping'


class EnglishSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    synset_words = models.CharField(max_length=1000, blank=True, null=True)
    gloss = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'english_synset_data'
        unique_together = (('synset_id', 'category'),)


class EnglishSynsetData1(models.Model):
    synset_id = models.IntegerField()
    category = models.CharField(max_length=100)
    synset_words = models.CharField(max_length=1000, blank=True, null=True)
    gloss = models.CharField(max_length=1000, blank=True, null=True)
    head = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'english_synset_data1'


class IdMapping(models.Model):
    mapping_id = models.AutoField(primary_key=True)
    hindi_id = models.CharField(max_length=11)
    hindi_category = models.CharField(max_length=20)
    english_id = models.CharField(max_length=11)
    english_category = models.CharField(max_length=20)
    comments = models.CharField(max_length=4048, blank=True, null=True)
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'id_mapping'
        unique_together = (('hindi_id', 'hindi_category', 'english_id', 'english_category'),)


class IdMapping2(models.Model):
    mapping_id = models.AutoField(primary_key=True)
    hindi_id = models.CharField(max_length=11)
    hindi_category = models.CharField(max_length=20)
    english_id = models.CharField(max_length=11)
    english_category = models.CharField(max_length=20)
    comments = models.CharField(max_length=4048, blank=True, null=True)
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'id_mapping2'
        unique_together = (('hindi_id', 'hindi_category', 'english_id', 'english_category'),)


class TblAllAssameseSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_assamese_synset_data'


class TblAllBengaliSynsetData(models.Model):
    synset_id = models.CharField(primary_key=True, max_length=11)
    head = models.CharField(max_length=255, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_bengali_synset_data'


class TblAllBodoSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_bodo_synset_data'


class TblAllEnglishSynsetData(models.Model):
    synset_id = models.IntegerField()
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.CharField(max_length=1000, blank=True, null=True)
    gloss = models.CharField(max_length=1000, blank=True, null=True)
    category = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_all_english_synset_data'


class TblAllGujaratiSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_gujarati_synset_data'


class TblAllHindiSynsetData(models.Model):
    synset_id = models.IntegerField()
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_hindi_synset_data'


class TblAllHindiSynsetDataOld(models.Model):
    synset_id = models.IntegerField()
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_hindi_synset_data_old'


class TblAllKannadaSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_kannada_synset_data'


class TblAllKashmiriSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_kashmiri_synset_data'


class TblAllKonkaniSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_konkani_synset_data'


class TblAllMalayalamSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_malayalam_synset_data'


class TblAllManipuriSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_manipuri_synset_data'


class TblAllMarathiSynsetData(models.Model):
    synset_id = models.IntegerField()
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.CharField(max_length=250, blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_marathi_synset_data'


class TblAllMeiteiSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_meitei_synset_data'


class TblAllNepaliSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_nepali_synset_data'


class TblAllOriyaSynsetData(models.Model):
    synset_id = models.CharField(primary_key=True, max_length=11)
    head = models.CharField(max_length=255, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_oriya_synset_data'


class TblAllPunjabiSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_punjabi_synset_data'


class TblAllSanskritSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_sanskrit_synset_data'


class TblAllSynsetData(models.Model):
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    synset_id = models.IntegerField()
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_synset_data'


class TblAllTamilSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_tamil_synset_data'


class TblAllTeluguSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_telugu_synset_data'


class TblAllUrduSynsetData(models.Model):
    synset_id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    synset = models.TextField(blank=True, null=True)
    gloss = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_all_urdu_synset_data'
