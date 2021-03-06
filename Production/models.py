# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import common

class Material(models.Model):
    Name = models.CharField(max_length=255)
    IconAssetID = models.CharField(max_length=255)
    SizeType = models.IntegerField(choices=common.SizeTypeChoices)
    StackSize = models.IntegerField()
    BuyPrice = models.IntegerField()
    SellPrice = models.IntegerField()

    def getJsonObject(self):
        return {
            "Name":self.Name,
            "IconAssetID":self.IconAssetID,
            "SizeType":self.SizeType,
            "StackSize":self.StackSize,
            "BuyPrice":self.BuyPrice,
            "SellPrice":self.SellPrice
        }
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __unicode__(self):
        return unicode(self.Name)

class ModuleStepInputMaterialAmount(models.Model):
    Material = models.ForeignKey(Material)
    Amount = models.IntegerField()
    ModuleStep = models.ForeignKey("ModuleStep", related_name="InputMaterials")

    def getJsonObject(self):
        return {
            "MaterialID":self.Material.id,
            "Amount":self.Amount,
        }
    
    class Meta:
        verbose_name = 'Input Material'
        verbose_name_plural = 'Input Materials'

    def __unicode__(self):
        return u"%d x %s" %(self.Amount, unicode(self.Material))

class ModuleStepOutputMaterialAmount(models.Model):
    Material = models.ForeignKey(Material)
    Amount = models.IntegerField()
    ModuleStep = models.ForeignKey("ModuleStep", related_name="OutputMaterials")

    def getJsonObject(self):
        return {
            "MaterialID": self.Material.id,
            "Amount": self.Amount,
        }
    
    class Meta:
        verbose_name = 'Output Material'
        verbose_name_plural = 'Output Materials'

    def __unicode__(self):
        return u"%d x %s" % (self.Amount, unicode(self.Material))

class ModuleSlotType(models.Model):
    Name = models.CharField(max_length=255)
    IsOptional = models.BooleanField()

    def getJsonObject(self):
        return {
            "Name":self.Name,
            "IsOptional":self.IsOptional,
        }
    
    class Meta:
        verbose_name = 'Module Slot Type'
        verbose_name_plural = 'Module Slot Types'

    def __unicode__(self):
        if self.IsOptional:
            return u"%s (optional)" % unicode(self.Name)
        else:
            return unicode(self.Name)

class ModuleStep(models.Model):
    Module = models.ForeignKey("Module", related_name="Steps")
    StepNumber = models.IntegerField(blank=False, default=0)

    def getJsonObject(self):
        inputMaterials = []
        for inMat in self.InputMaterials.all():
            inputMaterials.append(inMat.getJsonObject())
        outputMaterials = []
        for outMat in self.OutputMaterials.all():
            outputMaterials.append(outMat.getJsonObject())
        return {
            "InputMaterials":inputMaterials,
            "OutputMaterials":outputMaterials,
        }
    
    class Meta:
        verbose_name = 'Module Step'
        verbose_name_plural = 'Module Steps'

    def __unicode__(self):
        return u"Step %d %s" % (self.StepNumber, self.Module)

class Module(models.Model):
    Name = models.CharField(max_length=255)
    IconAssetID = models.CharField(max_length=255)
    FitsIntoSlot = models.ForeignKey(ModuleSlotType, related_name="FittingModule")

    def getJsonObject(self):
        steps = []
        for step in self.Steps.all():
            steps.append(step.getJsonObject())
        return {
            "Name":self.Name,
            "IconAssetID":self.IconAssetID,
            "FitsIntoSlot":self.FitsIntoSlot.id,
            "Steps":steps
        }
    
    def getJsonStepRecipes(self):
        stepRecipes = []
        totalSteps = self.Steps.count()
        stepNum = 1
        for step in self.Steps.all():
            stepRecipeJson = {
                "Name": "%s step %d/%d" % (self.Name, stepNum, totalSteps),
            }
            stepJson = step.getJsonObject()
            stepRecipeJson["InputMaterials"] = stepJson["InputMaterials"]
            stepRecipeJson["OutputMaterials"] = stepJson["OutputMaterials"]
            # this is super temporary, for the modulestep to recipe conversion!
            stepRecipeJson["id"] = step.id
            stepRecipes.append(stepRecipeJson)
            stepNum = stepNum + 1
        return stepRecipes
    
    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __unicode__(self):
        return u"%s (Slot: %s)" %(unicode(self.Name),unicode(self.FitsIntoSlot))

class ProductType(models.Model):
    Name = models.CharField(max_length=255)
    IconAssetID = models.CharField(max_length=255)
    BigImageAssetID = models.CharField(max_length=255)
    Slots = models.ManyToManyField(ModuleSlotType, related_name="UsedInProductType")

    def getJsonObject(self):
        slots = []
        for slot in self.Slots.all():
            slots.append(slot.id)
        return {
            "Name":self.Name,
            "IconAssetID":self.IconAssetID,
            "BigImageAssetID":self.BigImageAssetID,
            "SlotTypes":slots,
        }
    
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'

    def __unicode__(self):
        return unicode(self.Name)
