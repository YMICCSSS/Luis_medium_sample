########### Python 3.6 #############

#
# This quickstart shows how to predict the intent of an utterance by using the LUIS REST APIs.
#

import requests

try:

    ##########
    # Values to modify.

    # YOUR-APP-ID: The App ID GUID found on the www.luis.ai Application Settings page.
    appId = '放你自己的唷'

    # YOUR-PREDICTION-KEY: Your LUIS authoring key, 32 character value.
    prediction_key = '放你自己的唷'

    # YOUR-PREDICTION-ENDPOINT: Replace with your authoring key endpoint.
    # For example, "https://westus.api.cognitive.microsoft.com/"
    prediction_endpoint = '放你自己的唷'

    # 放入你要預測的分類
    # The utterance you want to use.
    utterance = '放入要預測的分類'
    ##########


    # The headers to use in this REST call.
    headers = {
    }


    # The URL parameters to use in this REST call.
    params ={
        'query': utterance,
        'timezoneOffset': '0',
        'verbose': 'true',
        'show-all-intents': 'true',
        'spellCheck': 'false',
        'staging': 'false',
        'subscription-key': prediction_key
    }


    # Make the REST call.
    response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict', headers=headers, params=params)
    response = response.json()
    # Display the results on the console.
    #印出第一個可能的分類
    print(response.get("prediction").get("topIntent"))

    #印出第二可能的分類
    print(list(response.get("prediction").get("intents").items())[1][0])



except Exception as e:
    # Display the error string.
    print(f'{e}')

