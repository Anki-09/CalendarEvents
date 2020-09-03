from flask import Flask,request,jsonify
app=Flask(__name__)
event_list=[{'event': 'Webinar on Aerospace',
                   'presenter':'Mr.Anandh Jogi',
                   'place':'Memorial hall,Jeppu',
                   'date':'14/01/2021',
                   'time':'9:30'},
                    {'event':'Workshop on git',
                     'presenter':'Mr.Vinod Gowda',
                     'place':'Father Fred hall,Mangalore',
                     'date':'24/01/2021',
                     'time':'11:30'},
                   {'event': 'Tedx Talk',
                   'presenter':'Mr.Hithesh Kumar',
                   'place':'Conference Hall,Vamanjoor',
                   'date':'20/02/2021',
                   'time':'20:00'},
                    {'event':'Webinar to AI',
                     'presenter':'Mr.Rahul',
                     'place':'Memorial  Hall,Jeppu',
                     'date':'28/03/2021',
                     'time':'10:30'},
                  {'event': 'IEEE Meeting for IEEE members',
                  'presenter':'Ms.Smriti Rai',
                  'place':'Conference hall,Vamanjoor',
                  'date':'02/04/2021',
                  'time':'11:00'},
                  {'event':'Webinar on BigData',
                   'presenter':'Mr.Anush Tripal',
                   'place':'Silver Bells,Mangalore',
                   'date':'11/05/2021',
                   'time':'9:00'},
                  {'event': 'Workshop on AWS',
                   'presenter':'Ms.Revati',
                   'place':'TMA Pai,Mangalore',
                   'date':'21/06/2021',
                   'time':'9:30'},
                    {'event':'Webinar on DataScience',
                     'presenter':'Ms.Shivani Singh',
                     'place':"Memorial Hall,Jeppu",
                     'date':'24/07/2021',
                     'time':'10:30'},
                    {'event':'Workshop on Cyber Security',
                     'presenter':'Mr.Ananth Prabhu',
                     'place':'Kudmul Rangarao Town Hall,Mangalore',
                     'date':'24/08/2021',
                     'time':'16:30'},
                   {'event': "Talk on 'The Greatest machine that never was'",
                   'presenter':'Ms.Amulya Shetty',
                    'place':'Father Fred hall,Mangalore',
                   'date':'12/09/2021',
                   'time':'10:00'},
                    {'event':'Webinar on Digital Transformation',
                     'presenter':'Mr.Suraj Rao',
                     'place':'Infosys,Mangalore',
                     'date':'24/07/2021',
                     'time':'9:00'},
                   {'event': 'Webinar on Placements2020',
                   'presenter':'Mr.Ananth',
                   'place':'Conference Hall,Mangalore',
                   'date':'11/04/2021',
                   'time':'12:30'},
                    {'event':'Workshop on Cloud Computing',
                     'presenter':'Mr.Rohan Gowda',
                     'place':'Father Fred hall,Mangalore',
                     'date':'25/05/2021',
                     'time':'13:30'},
                   {'event': 'Workshop on RC Aircraft Design',
                   'presenter':'Mr.Ananth Shetty',
                   'place':'Memorial hall,Jeppu',
                   'date':'1/11/2021',
                   'time':'10:30'},
                    {'event':'Workshop on 3D Printing',
                     'presenter':'Mr.Vinod Poojary',
                     'place':'Father Fred hall,Mangalore',
                     'date':'29/12/2021',
                     'time':'11:30'},
                   {'event': "Talk on 'Sanitation is the basic human right'",
                   'presenter':'Ms.Rohan Shetty',
                   'place':'Town Hall,Mangalore',
                   'date':'12/06/2021',
                   'time':'10:00'},
                    {'event':'Workshop on Hovercraft',
                     'presenter':'Mr.Vignesh Prasad',
                     'place':'Father Fred hall,Mangalore',
                     'date':'24/03/2021',
                     'time':'11:30'},
                    {'event':'Webinar on Renewable energy',
                     'presenter':'Mr.Suraj Rai',
                     'place':'Conference Hall,Vamanjoor',
                     'date':'24/08/2021',
                     'time':'11:30'},
                    {'event': 'Webinar on Detterence',
                   'presenter':'Mr.Nithesh Jogi',
                   'place':'Memorial hall,Jeppu',
                   'date':'14/10/2021',
                   'time':'9:30'},
                    {'event':'Webinar on Magnetic Materials',
                     'presenter':'Ms.Amitha',
                     'place':'Father Fred hall,Mangalore',
                     'date':'24/12/2021',
                     'time':'11:30'}]
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
