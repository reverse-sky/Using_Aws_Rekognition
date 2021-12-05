
import boto3

def make_polly(photo, bucket,file_name):
        client=boto3.client('rekognition')
        polly =boto3.client("polly", region_name="us-east-1")
        response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
        textDetections=response['TextDetections']
        print (f'Analying image[{photo}]......done:')
        tlist = []
        for text in textDetections:
            if 'ParentId' not in text:        
                tlist.append(text['DetectedText'])
        # print ('Detected text:' + text['DetectedText'])
        # print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        # print ('Id: {}'.format(text['Id']))
        sentence = ' '.join(tlist)
        response2 =polly.synthesize_speech(Text=sentence, OutputFormat="mp3",VoiceId="Joanna")        
        print("Sentence found: ",sentence)    
        file_name = file_name
        file = open(f'{file_name}.mp3','wb')
        file.write(response2['AudioStream'].read())
        file.close()
        return f"Audio output: {file_name}"
