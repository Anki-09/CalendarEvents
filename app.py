from flask import Flask,request,jsonify
app=Flask(__name__)
event_list=[{'event': 'Webinar on Computer Science as future',
                   'presenter':'Mr.Anandh Jogi',
                   'place':'Memorial hall,Jeppu',
                   'date':'14/01/2021',
                   'time':'9:30'},
                    {'event':'Webinar on AI',
                     'presenter':'Mr.Rahul',
                     'place':'Memorial  Hall,Jeppu',
                     'date':'28/03/2021',
                     'time':'10:30'},
                    {'event':'Webinar on DataScience',
                     'presenter':'Ms.Shivani Singh',
                     'place':"Memorial Hall,Jeppu",
                     'date':'24/07/2021',
                     'time':'10:30'},
                    {'event':'Workshop on Cloud Computing',
                     'presenter':'Mr.Rohan Gowda',
                     'place':'Father Fred hall,Mangalore',
                     'date':'25/05/2021',
                     'time':'13:30'}]
quiz_list=[[{'Qno':1,
                 'Question':'Which among the following is not a computer language',
                 'option A':'ALGOL',
                 'option B':'COBOL',
                 'option C':'PASCAL',
                 'option D':'DRAM'},
                 {'Qno':2,
                  'Question':'Which among the following is used in creating a chart',
                 'option A':'Chart Wizard',
                 'option B':'Computing Wizard',
                 'option C':'Calculating Wizard',
                 'option D':'Data Wizard'},
                 {'Qno':3,
                  'Question':'Which among the following is a communication system that transfers data between components inside a computer',
                 'option A':'Bus',
                 'option B':'RAM',
                 'option C':'Processor',
                 'option D':'LAN'}],
                 [{'Qno':1,
                 'Question':'KEE is a product of',
                 'option A':'IntelliCorpn',
                 'option B':'Teknowledge',
                 'option C':'Texas Instruments',
                 'option D':'Tech Knowledge'},
                 {'Qno':2,
                  'Question':'Default reasoning is another type of',
                 'option A':'Analogical reasoning',
                  'option B':'Bitonic reasoning',
                 'option C':'Non-monotonic reasoning',
                 'option D':'Monotonic reasoning'},
                 {'Qno':3,
                     'Question':'If a robot can alter its own trajectory in response to external conditions,it is considered to be:',
                 'option A':'mobile',
                 'option B':'open loop',
                 'option C':'intelligent',
                 'option D':'non-servo'}],
                 [{'Qno':1,
                 'Question':'Point out the correct statement',
                 'option A':'Raw data is original source of data',
                 'option B':'Preprocessed data is original source of data',
                 'option C':'Raw data is the data obtained after processing steps',
                 'option D':'None of the mentioned'},
                 {'Qno':2,
                  'Question':'Which of the following is performed by Data Scientist',
                 'option A':'Define the question',
                 'option B':'Create reproducible code',
                 'option C':'Challenge results',
                 'option D':'All of the mentioned'},
                 {'Qno':3,
                     'Question':'Which of the following is the most important language for Data Science',
                 'option A':'Java',
                 'option B':'Ruby',
                 'option C':'R',
                 'option D':'None of the mentioned'}],
                 [{'Qno':1,
                 'Question':'Which of the following is essential concept related to Cloud',
                 'option A':'Reliability',
                 'option B':'Productivity',
                 'option C':'Abstraction',
                 'option D':'All of the mentioned'},
                 {'Qno':2,
                  'Question':'Point out the wrong statement',
                 'option A':'All applications benefit from deployment in the cloud',
                 'option B':'With cloud computing,you can start very small and become very big very fast',
                 'option C':'Cloud computing is revolutionary,even if the technology it is built on is evolutionary',
                 'option D':'None of the mentioned'},
                 {'Qno':3,
                     'Question':'Which of the following cloud concept is related to pooling and sharing of resources',
                 'option A':'Polymorphism',
                 'option B':'Abstraction',
                 'option C':'Virtualization',
                 'option D':'None of the mentioned'}]]
@app.route('/events', methods=['GET','POST'])
def events():
    if request.method =='GET':
       if len(event_list)>0:
            return jsonify(event_list)
        else:
            'Nothing Found',404
    if request.method=='POST':
        new_event=request.form['event']
        new_presenter=request.form['presenter']
        new_place=request.form['place']
        new_date=request.form['date']
        new_time=request.form['time']

        for eve in event_list:
            if eve['date']==new_date and eve['time']==new_time and eve['place']==new_place:
                return "Please change the venue or the timings of the event."+eve['event']+" is conducted at "+eve['place']+" at the same time."

        new_obj={
                'event':new_event,
                'presenter':new_presenter,
                'place':new_place,
                'date':new_date,
                'time':new_time
                }
        event_list.append(new_obj)
        return jsonify(event_list)

@app.route('/events/<event>', methods=['GET','PUT','DELETE'])
def one_event(event):
    if request.method=='GET':
        for eve in event_list:
            if eve['event']==event:
                return jsonify(eve)
    if request.method=='PUT':
        for eve in event_list:
            if eve['event']==event:
                eve['presenter']=request.form['presenter']
                new_place=request.form['place']
                new_date=request.form['date']
                new_time=request.form['time']
                for eve in event_list:
                    if eve['date']==new_date and eve['time']==new_time and eve['place']==new_place:
                         return "Please change the venue or the timings of the event."+eve['event']+" is conducted at "+eve['place']+" at the same time."
                eve['place']=new_place
                eve['date']=new_date
                eve['time']=new_time
                updated_event={
                        'event':event,
                        'presenter':eve['presenter'],
                        'place':eve['place'],
                        'date':eve['date'],
                        'time':eve['time']
                        }
                return jsonify(updated_event)
    if request.method=='DELETE':
        for index,eve in enumerate(event_list):
            if eve['event']==event:
                event_list.pop(index)
                return jsonify(event_list)

@app.route('/events/quiz/<event>',methods=['GET','POST'])
def quiz(event):
    if request.method=='GET':
        i=0
        for eve in event_list:
            i=i+1
            if eve['event']==event:
                return jsonify(quiz_list[i])

    if request.method=='POST':
       ans1=request.form['ans1']
       ans2=request.form['ans2']
       ans3=request.form['ans3']
       yes='Congratulations!You are ready to attend '+event
       no='Sorry..:(,You are not ready to attend '+event+'. Please go through the basics of the concept before attending the webinar.'
       if event=='Webinar on Computer Science as future':
           if ans1=='option D' and ans2=='option A' and ans3=='option A':
               return yes
           return no
       if event=='Webinar on AI':
           if ans1=='option A' and ans2=='option C' and ans3=='option C':
               return yes
           return no
       if event=='Webinar on Data Science':
           if ans1=='option A' and ans2=='option D' and ans3=='option C':
               return yes
           return no
       if event=='Workshop on Cloud Computing':
           if ans1=='option C' and ans2=='option A' and ans3=='option C':
               return yes
           return no
