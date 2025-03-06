from django.shortcuts import render,redirect
from .models import Stations,KLM
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import qrcode
import cv2
# Create your views here.

def index(request):
    
    return render(request,'index.html')

def travel(request):
    stations = Stations.objects.all()
    print(stations)
    context = {'stations':stations}
    if request.method == 'POST':
        from_station = request.POST.get('from')
        to_station = request.POST.get('to')
        mail = request.POST.get('mail')
        print(from_station,to_station,mail)
        # mail__string = mail.split('@gmail.com')[0] 
        data = f"{mail}, {from_station}, {to_station}"
        Qrcode = qrcode.make(data)
        Qrcode.save('./app/static/app_images/qrcode.png')
        print(from_station, to_station, mail)
        if from_station and to_station and mail:
            from_db = Stations.objects.get(station = from_station)
            to_db = Stations.objects.get(station = to_station)
            print(from_db.station,from_db.id)
            from_id = int(from_db.id)
            to_id = int(to_db.id)
            kms_db = KLM.objects.all()
            if from_id < to_id:   
                total_kms = sum([obj.klm for obj in kms_db if obj.id>=from_id and obj.id <= to_id-1])  
            elif from_id > to_id:
                total_kms = sum([obj.klm for obj in kms_db if obj.id>=to_id and obj.id <= from_id-1])
            print(f'total kilometers is {total_kms}')
            petrol_saved = total_kms*0.05857
            carbon_emmission = petrol_saved * 2.3 # kg of carbon emmission
            carbon_emmission = carbon_emmission * 1000 # In grams we need to convert kg into grams.
            print(f'total fuel saved in this journey {round(petrol_saved,2)} liters ')   
            petrol_price = petrol_saved * 109
            print(f'fule price which you have saved is {round(petrol_price,2)}')
            total_ticket_price = petrol_price / 2 
            print(f'total ticket price for your journey is {round(total_ticket_price,2)}')
            try:
                # send_mail('SENDING MAIL',f'YOU GOT REGISTERED',settings.EMAIL_HOST_USER,[mail]) #(subj, mesg, host_mail, [recever mail])
                email = EmailMessage(
                                subject=f'{"*"*10} METRO TICKET {"*"*10}',
                                body=f'Hope you will have a safe and happy journey from {from_station} to {to_station}\nTotal fuel saved by this journey is {round(petrol_saved,2)} liters \n--> Total journey is {round(total_kms,2)} kms and carbon emmission saved is "{round(carbon_emmission,2)} grams of CO₂"\nTotal ticket price for this journey is {round(total_ticket_price,2)} rupees',
                                from_email=settings.EMAIL_HOST_USER,
                                to=[mail],
                            ) 

                email.attach_file('./app/static/app_images/qrcode.png') 
                email.send() 
                print('mail sended') 
                return redirect('index') 
            except Exception as e:
                print(f'{e} exception has raised..')

    return render(request,'travel.html',context)

def validate(request):
    
    return render(request,'validate.html')

def entry_from(request):
    stations = Stations.objects.all()
    print(stations)
    context = {'stations':stations,
               'result':''}
    if request.method == "POST":
        entry_station = request.POST.get('entry_station')
        # Initialize the camera
        cap = cv2.VideoCapture(0)

        # Initialize the QRCode detector
        detector = cv2.QRCodeDetector()
        d={'mail':'','from':'','to':''}
        print("Point the camera at a QR Code.")

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            print(frame)
            if not ret:
                break

            # Detect and decode
            data, bbox, _ = detector.detectAndDecode(frame)

            if data:
                print("QR Code Data:", data)
                for k,v in zip(d,data.split(',')):
                    d[k] = v.strip()
                print(d)
                break  # Exit after detecting a QR code

            # Display the frame
            cv2.imshow("QR Code Scanner", frame)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()
        if d['from'] == entry_station:
            context['result'] = f"Welcome To {d['from']}"
            print('success')
        else:
            context['result'] = f"Please go to the {d['from']} station for entry"
    return render(request,'entry_form.html',context)

def exit_form(request):
    stations = Stations.objects.all()
    print(stations)
    context = {'stations':stations,
               'result':''}
    if request.method == "POST":
        exit_station = request.POST.get('exit_station')
        print(exit_station)
        # Initialize the camera
        cap = cv2.VideoCapture(0)

        # Initialize the QRCode detector
        detector = cv2.QRCodeDetector()
        d={'mail':'','from':'','to':''}
        print("Point the camera at a QR Code.")

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                break

            # Detect and decode
            data, bbox, _ = detector.detectAndDecode(frame)

            if data:
                print("QR Code Data:", data)
                for k,v in zip(d,data.split(',')):
                    d[k] = v.strip()
                print(d)
                break  # Exit after detecting a QR code

            # Display the frame
            cv2.imshow("QR Code Scanner", frame)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()
        if d['to'] == exit_station:
            context['result'] = f"Thank You for traveling from {d['from']} to {d['to']}"
            print('success')
        else:
            context['result'] = f"Please go to the {d['to']} station for exit"

    return render(request,'exit_form.html',context)