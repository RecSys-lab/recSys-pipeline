from PyInquirer import prompt
from config import datasets, models, fusions

modelChoices = []
fusionChoices = []
datasetChoices = []


def parametersToChoices():
    # Preparing model items
    for model in models:
        modelChoices.append(model)
    # Preparing dataset items
    for dataset in datasets:
        datasetChoices.append(dataset)
    # Preparing fusion items
    for fusion in fusions:
        fusionChoices.append(fusion)


def getUserInput():
    # Initiate choices
    parametersToChoices()
    # Appy choices to the questions
    questions = [
        {
            'type': 'list',
            'name': 'Model',
            'message': 'Choose the model you need:',
            'choices': modelChoices
        },
        {
            'type': 'list',
            'name': 'Dataset',
            'message': 'Choose the dataset you need:',
            'choices': datasetChoices
        },
        {
            'type': 'list',
            'name': 'Fusion',
            'message': 'Choose the fusion you need:',
            'choices': fusionChoices
        },
        {
            'type': 'confirm',
            'message': 'Do you confirm your selected choices?',
            'name': 'Confirmation',
            'default': True,
        },
    ]
    # Showing the selected items to the user
    userInputs = prompt(questions)
    return userInputs


def validateUserItems():
    userInputs = getUserInput()
    confirmation = userInputs['Confirmation']
    if (confirmation == True):
        print('Validating your choices ...')
        selectedModelScopes = models[userInputs['Model']]
        selectedDatasetScopes = datasets[userInputs['Dataset']]
        # Checking if dataset covers all scopes of models
        isCovered = all(
            item in selectedDatasetScopes for item in selectedModelScopes)
        if (isCovered):
            print('Model matches dataset scopes')
            return userInputs
        else:
            difference = [
                item for item in selectedDatasetScopes if item not in selectedModelScopes]
            print(f'Selected model does not contain {difference} scope(s)!')
    else:
        print('See you later!')
