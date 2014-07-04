from django import template
import pdb

register = template.Library()

@register.filter(name='percentage')
def percentage(answer_objects, index):
    #value is the list of all the objects
    #arg is the index of the 
    local_votes = answer_objects[index - 1].votes
    total_votes = 0

    for obj in answer_objects:
        total_votes += obj.votes

    #pdb.set_trace()
    if(total_votes == 0):
        return 0

    return (local_votes*100)//total_votes

@register.filter(name="count_votes")
def count_votes(object_list):
    count = 0
    for obj in object_list:
        count += obj.votes

    return count

@register.filter(name="calc_average")
def calc_average(object_list):
    vote_sum = 0.0
    vote_count = 0
    for (counter,obj) in enumerate(object_list):
        vote_sum += (counter + 1) * obj.votes
        vote_count += obj.votes

    if(vote_count == 0):
        return 0
    
    return  (float) ((vote_sum*100)//vote_count)/100

@register.filter
def mod_calc(n):
    return (n - 1)%3


@register.filter
def get_emotion_image(emotion):
    if(emotion== 'joy'):
        return 'http://theumbrellaagency.com/wp-content/uploads/2009/07/umbrella_agency_smiley_face-200x200.jpg'
    elif (emotion == 'hope'):
        return 'http://twilight.ponychan.net/chan/arch/src/130751482204.png'
    elif (emotion == 'sorrow'):
        return 'data:image/jpeg;base64,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'
    elif (emotion == 'distress'):
        return 'http://rocknrollghost.com/wp-content/uploads/2012/04/02SHAME-articleLarge-v2-200x200.jpg'
    else: 
        return 'NO CORRESPONDING IMAGE'
