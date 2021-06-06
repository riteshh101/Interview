from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.response import Response
from app.serializers import *
# Create your views here.

class studentRegister(ViewSet):
    def create(self,request):
        data=request.data
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        address = data.get('address')
        if name == "" or name == None or email == "" or email == None or password == "" or password == None or address == "" or address == None:
            return Response({'response_code':200,'comments':'something missing please check',"status":False})
        else:
            obj = candidate(name=name,email=email,password=make_password(password),address=address)
            obj.save()
            response_data = {'response_code':200,'comments':'user register successfully',"status": True}
            return Response(response_data)


class student_login(ViewSet):
    def create(selfself,request):
        data=request.data
        email=data.get('email')
        password=data.get('password')
        if email == None or password == None or email == '' or password=="":
            response_data = {'response_code':200,'comments':'something missing please check',"status": False}
            return Response (response_data)
        else:
            try:
                user_obj=candidate.objects.get(email=email)

                if check_password(password,user_obj.password):

                    d = {}
                    d['id'] = user_obj.id
                    d['name'] = user_obj.name
                    d['email'] = user_obj.email
                    d['address'] = user_obj.address
                    response_data = {'user_data':d,'response_code': 200, 'comments': 'Login Successfully',
                                     "status": True}
                    return Response(response_data)
                else:
                    response_data = {'response_code': 200, 'comments': 'password not correct..',
                                     "status": False}
                    return Response(response_data)


            except:
                response_data = {'response_code':200,'comments':'Invalid email try correct email',"status": False}
                return Response(response_data)


class TestScore(ViewSet):
    def create(self,request):
        data = request.data
        id = data.get('id')
        first_round_score = data.get('first_round_score')
        second_round_score = data.get('second_round_score')
        third_round_score = data.get('third_round_score')
        if id=="" or id==None or first_round_score=="" or first_round_score == None or second_round_score=="" or second_round_score==None or third_round_score=="" or third_round_score==None:
            response_data = {'response_code': 200, 'comments': 'something missing please check', "status": False}
            return Response(response_data)

        else:
            if first_round_score<=10 and second_round_score<=10 and third_round_score<=10:
                try:
                    user_instance = candidate.objects.get(id=id)
                    try:
                        check = test_score.objects.get(candi=user_instance)
                        response_data = {'response_code': 200, 'comments': 'Score already added',
                                         "status": True}
                        return Response(response_data)
                    except:
                        obj = test_score(candi=user_instance,first_round_score=first_round_score,second_round_score=second_round_score,third_round_score=third_round_score)
                        obj.save()
                        response_data = {'response_code': 200, 'comments': 'Student score saved successfully', "status": True}
                        return Response(response_data)
                except:
                    response_data = {'response_code': 200, 'comments': 'Invalid User id', "status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code': 200, 'comments': 'Please Score provide under 10', "status": False}
                return Response(response_data)


class highest_score_AvgScore(ViewSet):
    def list(self,request):
        # highest scoring candidate
        test_obj = test_score.objects.all()
        d={}
        for x in test_obj:
            d[x.candi.name]=x.first_round_score+x.second_round_score+x.third_round_score
        max_key = max(d, key=d.get)
        highest = {}
        highest[max_key]=d[max_key]
        # Avg score per round
        first = 0
        second = 0
        third = 0
        for x in test_obj:
            first = first + x.first_round_score
            second = second + x.second_round_score
            third = third + x.third_round_score
        first_round = first / len(test_obj)
        second_round = second / len(test_obj)
        third_round = third / len(test_obj)
        d = {"first_round_average": first_round, "second_round_average": second_round,
             "third_round_average": third_round}
        response_data = {'highest_scoring_candidate':highest,'per_round_avg_score':d,'response_code': 200, 'comments': 'Highest Scoring Candidate', "status": True}
        return Response(response_data)




class show_all_candidate(ViewSet):
    def list(self,request):
        candi_obj= candidate.objects.all()
        seriler = CandidateSerializers(candi_obj, many=True)
        response_data = {'candidate': seriler.data, 'response_code': 200, 'comments': 'all candidate',
                         "status": True}
        return Response(response_data)

    def update(self,request,**kwargs):
        data= request.data
        id = data.get('id')
        address = data.get('address')
        try:
            user_obj = candidate.objects.get(id=id)
            if address =='' or address==None:
                response_data = {'response_code': 200, 'comments': 'address missing please check', "status": False}
                return Response(response_data)
            else:
                user_obj.address = address
                user_obj.save()
                d={}
                d['id'] = user_obj.id
                d['name'] = user_obj.name
                d['email'] = user_obj.email
                d['address'] = user_obj.address
                response_data = {'user_data':d,'response_code': 200, 'comments': 'address updated successfully', "status": True}
                return Response(response_data)
        except:
            response_data = {'response_code': 200, 'comments': 'Invalid Student Id', "status": False}
            return Response(response_data)


