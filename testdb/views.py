from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post, Focal, Report, Paper, stations
from django.contrib.auth.models import User
from .forms import FileForm, FileForm2, FileForm1, FileForm11, ImageForm, ImageForm2, NameForm, FocalForm, ContactForm, ReportForm, PaperForm
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("testdb-home")
      
	form = ContactForm()
	return render(request, "testdb/contact.html", {'form':form})


def upload(request):
	form = FileForm(request.POST, request.FILES)
	form = FileForm1(request.POST, request.FILES)
	form = FileForm11(request.POST, request.FILES)
	form = FileForm2(request.POST, request.FILES)
	form = ImageForm(request.POST, request.FILES)
	form = ImageForm2(request.POST, request.FILES)
	form = NameForm(request.POST)
	if request.method =='POST':
		if form.is_valid():
			Region = request.POST['Region']
			MagnitudeMw = request.POST['MagnitudeMw']
			upload_image = request.FILES['image']
			upload_image2 = request.FILES['image2']
			upload_file = request.FILES['file']

			upload_file1 = request.FILES['file1']
			upload_file11 = request.FILES['file11']

			upload_file2 = request.FILES['file2']
			lines = upload_file.read()
			lines1 = upload_file1.readlines()
			lines11 = upload_file11.readlines()


			station = []
			comp = []
			DIS = []
			AZM = []
			ARR_TIME = []
			RES = []
			PHASE = []
			
			
			station_m = []
			comp_m = []
			DIS_m = []
			azm_m = []
			b_azm_m = []
			amp_m  = []
			gain_m  = []
			local_m_m  = []


			station_m2 = []
			comp_m2 = []
			DIS_m2 = []
			azm_m2 = []
			b_azm_m2 = []
			amp_m2  = []
			gain_m2  = []
			local_m_m2  = []



			for line in lines1:
				parts = line.decode('utf-8').split()

				if len(parts) > 0:
					station_m.append(parts[0])  # 0th column
				if len(parts) > 1:
					comp_m.append(parts[1])     # 1st column
				if len(parts) > 2:
					DIS_m.append(parts[2])      # 2nd column
				if len(parts) > 3:
					azm_m.append(parts[3])      # 3rd column
				if len(parts) > 4:
					b_azm_m.append(parts[4])    # 4th column
				if len(parts) > 7:
					amp_m.append(parts[8])      # 7th column
				if len(parts) > 8:
					gain_m.append(parts[9])     # 8th column
				if len(parts) > 9:
					local_m_m.append(parts[7])  # 9th column

			# 5.380024, etc.

			# Now each list will store the respective values from all rows together.




			for line in lines11:
				parts = line.decode('utf-8').split()

				if len(parts) > 0:
					station_m2.append(parts[0])  # 0th column
				if len(parts) > 1:
					comp_m2.append(parts[1])     # 1st column
				if len(parts) > 2:
					DIS_m2.append(parts[2])      # 2nd column
				if len(parts) > 3:
					azm_m2.append(parts[3])      # 3rd column
				if len(parts) > 4:
					b_azm_m2.append(parts[4])    # 4th column
				if len(parts) > 7:
					amp_m2.append(parts[8])      # 7th column
				if len(parts) > 8:
					gain_m2.append(parts[9])     # 8th column
				if len(parts) > 9:
					local_m_m2.append(parts[7])  # 9th column
			# Example: '4.522512'


			Magnitude = local_m_m + local_m_m2/2
# Now you have separate lists for each value from the rows.

			
			# for line in lines1:
				
			# 	parts = line.decode('utf-8').split()

			# 	if parts:
			# 		station_m.append(parts[0])
			# 	if parts:
			# 		station_m.append(parts[1])
			# 	if parts:
			# 		station_m.append(parts[2])
			# 	if parts:
			# 		station_m.append(parts[3])
			# 	if parts:
			# 		station_m.append(parts[4])
			# 	if parts:
			# 		station_m.append(parts[5])
			# 	if parts:
			# 		station_m.append(parts[6])
			# 	if parts:
			# 		station_m.append(parts[7])
			# 	if parts:
			# 		station_m.append(parts[8])
			# 	if parts:
			# 		station_m.append(parts[9])
			# 	# if parts:
			# 	# 	station_m.append(parts[10])
			# 	# if parts:
			# 	# 	station_m.append(parts[11])
			# 	# if parts:
			# 	# 	station_m.append(parts[12])
			# 	# if parts:
			# 	# 	station_m.append(parts[13])
			# 	# if parts:
			# 	# 	station_m.append(parts[14])


			# 	if parts:
			# 		comp_m.append(parts)
			# 	if parts:
			# 		comp_m.append(parts[1])
			# 	if parts:
			# 		comp_m.append(parts[2])
			# 	if parts:
			# 		comp_m.append(parts[3])
			# 	if parts:
			# 		comp_m.append(parts[4])
			# 	if parts:
			# 		comp_m.append(parts[5])
			# 	if parts:
			# 		comp_m.append(parts[6])
			# 	if parts:
			# 		comp_m.append(parts[7])
			# 	if parts:
			# 		comp_m.append(parts[8])
			# 	if parts:
			# 		comp_m.append(parts[9])


			# 	if parts:
			# 		DIS_m.append(parts[0])
			# 	if parts:
			# 		DIS_m.append(parts[1])
			# 	if parts:
			# 		DIS_m.append(parts[2])
			# 	if parts:
			# 		DIS_m.append(parts[3])
			# 	if parts:
			# 		DIS_m.append(parts[4])
			# 	if parts:
			# 		DIS_m.append(parts[5])
			# 	if parts:
			# 		DIS_m.append(parts[6])
			# 	if parts:
			# 		DIS_m.append(parts[7])
			# 	if parts:
			# 		DIS_m.append(parts[8])
			# 	if parts:
			# 		DIS_m.append(parts[9])



			# 	if parts:
			# 		azm_m.append(parts[0])
			# 	if parts:
			# 		azm_m.append(parts[1])
			# 	if parts:
			# 		azm_m.append(parts[2])
			# 	if parts:
			# 		azm_m.append(parts[3])
			# 	if parts:
			# 		azm_m.append(parts[4])
			# 	if parts:
			# 		azm_m.append(parts[5])
			# 	if parts:
			# 		azm_m.append(parts[6])
			# 	if parts:
			# 		azm_m.append(parts[7])
			# 	if parts:
			# 		azm_m.append(parts[8])
			# 	if parts:
			# 		azm_m.append(parts[9])





			# 	if parts:
			# 		b_azm_m.append(parts[0])
			# 	if parts:
			# 		b_azm_m.append(parts[1])
			# 	if parts:
			# 		b_azm_m.append(parts[2])
			# 	if parts:
			# 		b_azm_m.append(parts[3])
			# 	if parts:
			# 		b_azm_m.append(parts[4])
			# 	if parts:
			# 		b_azm_m.append(parts[5])
			# 	if parts:
			# 		b_azm_m.append(parts[6])
			# 	if parts:
			# 		b_azm_m.append(parts[7])
			# 	if parts:
			# 		b_azm_m.append(parts[8])
			# 	if parts:
			# 		b_azm_m.append(parts[9])
				


			# 	if parts:
			# 		amp_m.append(parts[0])
			# 	if parts:
			# 		amp_m.append(parts[1])
			# 	if parts:
			# 		amp_m.append(parts[2])
			# 	if parts:
			# 		amp_m.append(parts[3])
			# 	if parts:
			# 		amp_m.append(parts[4])
			# 	if parts:
			# 		amp_m.append(parts[5])
			# 	if parts:
			# 		amp_m.append(parts[6])
			# 	if parts:
			# 		amp_m.append(parts[7])
			# 	if parts:
			# 		amp_m.append(parts[8])
			# 	if parts:
			# 		amp_m.append(parts[9])



			# 	if parts:
			# 		gain_m.append(parts[0])
			# 	if parts:
			# 		gain_m.append(parts[1])
			# 	if parts:
			# 		gain_m.append(parts[2])
			# 	if parts:
			# 		gain_m.append(parts[3])
			# 	if parts:
			# 		gain_m.append(parts[4])
			# 	if parts:
			# 		gain_m.append(parts[5])
			# 	if parts:
			# 		gain_m.append(parts[6])
			# 	if parts:
			# 		gain_m.append(parts[7])
			# 	if parts:
			# 		gain_m.append(parts[8])
			# 	if parts:
			# 		gain_m.append(parts[9])



			# 	if parts:
			# 		local_m_m.append(parts[0])
			# 	if parts:
			# 		local_m_m.append(parts[1])
			# 	if parts:
			# 		local_m_m.append(parts[2])
			# 	if parts:
			# 		local_m_m.append(parts[3])
			# 	if parts:
			# 		local_m_m.append(parts[4])
			# 	if parts:
			# 		local_m_m.append(parts[5])
			# 	if parts:
			# 		local_m_m.append(parts[6])
			# 	if parts:
			# 		local_m_m.append(parts[7])
			# 	if parts:
			# 		local_m_m.append(parts[8])
			# 	if parts:
			# 		local_m_m.append(parts[9])











			# for line in lines11:
			# 	parts = line.split()
			# 	station_m2.append(parts[0][0])
			# 	comp_m2.append(parts[0][1])
			# 	DIS_m2.append(parts[0][2])
			# 	azm_m2.append(parts[0][3])
			# 	b_azm_m2.append(parts[0][0])
			# 	amp_m2.append(parts[0][1])
			# 	gain_m2.append(parts[0][2])
			# 	local_m_m2.append(parts[0][3])			

			
			

			



			for item in lines.split(b"\n"):

				if b'RMS' in item:
					RMS = item[34:40].strip()
					RMS = RMS.decode()

				elif b'Latitude' in item:
					Latitude = item[32:40].strip()
					Latitude = Latitude.decode()
					lu1 = item[61:73].strip()
					lu1 = lu1.decode()
			        

				elif b'Longitude' in item:
					Longitude = item[32:40].strip()
					Longitude = Longitude.decode()
					lu2 = item[61:73].strip()
					lu2 = lu2.decode()

			        
				elif b'Depth' in item:
					Depth = item[34:40].strip()
					Depth = Depth.decode()

				elif b'Gap' in item:
					Gap = item[36:40].strip()
					Gap = Gap.decode()

				elif b'Event (OCAL)' in item:
					item1 = item[21:31].replace(b" ", b"-")
					item2 = item[32:40].replace(b" ", b":")
					item3 = item[40:44].replace(b" ", b".")
					event = item1 + b" " + item2 + item3
					event = event.decode()
			        
				# elif b'Magnitude' in item:
				# 	Magnitude = item[10:16]
				# 	Magnitude = Magnitude.decode()


				# elif b'MagnitudeMw' in item:
				# 	MagnitudeMw = item[15:19]
				# 	MagnitudeMw = MagnitudeMw.decode()
					


				elif b'KAR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('KAR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'SLY1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('SLY1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'AMR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('AMR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'AMR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('AMR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'BSR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('BSR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'BSR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('BSR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'NSR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'NSR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'NSR3' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR3')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)


				elif b'NSR4' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('NSR4')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'KIR1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('KIR1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'ANB1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('ANB1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)
					
				elif b'ANB2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('ANBB2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)
					
				elif b'DHK1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('DHK1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'SAM1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('SAM1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'SAM2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('SAM2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'DYL1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('DYL1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'BAG1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('BAG1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'KUT1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('KUT1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'TIK1' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('TIK1')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)

				elif b'KAR2' in item:
					zne = item[8:9]
					zne = zne.decode()
					station.append('KAR2')
					comp.append(zne)
					dis = item[11:17]
					dis = dis.decode()
					DIS.append(dis)
					azm = item[17:21]
					azm = azm.decode()
					AZM.append(azm)
					arr_time = item[28:32] + b'-' + item[32:34] + b'-' + item[34:36] + b' ' + item[36:38] + b':' + item[38:40] + b':' + item[40:46]
					arr_time = arr_time.decode()
					ARR_TIME.append(arr_time)
					res = item[55:59]
					res = res.decode()
					RES.append(res)
					phase = item[65:68]
					phase = phase.decode()
					PHASE.append(phase)
					

			current_user = request.user
			upload=Post(RMS=RMS, 
				lu1=lu1, lu2=lu2, 
				Latitude=Latitude, 
				Longitude=Longitude, 
				Depth=Depth, 
				event=event, 
				Gap=Gap, 
				Magnitude=Magnitude, 
				MagnitudeMw=MagnitudeMw,
				Region=Region, 
				image=upload_image,
				image2=upload_image2,
				file2=upload_file2,
				station_m=station_m,
				station_m2=station_m2,
				comp_m=comp_m,
				comp_m2=comp_m2,
				DIS_m=DIS_m,
				DIS_m2=DIS_m2,
				azm_m=azm_m,
				azm_m2=azm_m2,
				amp_m=amp_m,
				amp_m2=amp_m2,
				b_azm_m=b_azm_m,
				b_azm_m2=b_azm_m2,
				gain_m=gain_m,
				gain_m2=gain_m2,
				local_m_m=local_m_m,
				local_m_m2=local_m_m2,
				station=station, 
				comp=comp, 
				DIS=DIS, 
				AZM=AZM, 
				ARR_TIME=ARR_TIME, 
				RES=RES, 
				PHASE=PHASE,
				author=current_user, date_posted=event)
			upload.save()
			

	return render(request, 'testdb/post_form.html')




def upload_focal(request):
	form = FocalForm(request.POST, request.FILES)
	if request.method =='POST':
		if form.is_valid():
			title = request.POST['title']
			date = request.POST['date']
			file = request.FILES['file']

			current_user = request.user
			upload=Focal(title=title, file=file, author=current_user, date_posted=date, date=date)
			upload.save()
	return render(request, 'testdb/focal_form.html')


def upload_report(request):
	form = ReportForm(request.POST, request.FILES)
	if request.method =='POST':
		if form.is_valid():
			title = request.POST['title']
			date = request.POST['date']
			file = request.FILES['file']

			current_user = request.user
			upload=Report(title=title, file=file, author=current_user, date_posted=date, date=date)
			upload.save()
	return render(request, 'testdb/report_form.html')


def upload_paper(request):
	form = PaperForm(request.POST)
	if request.method =='POST':
		if form.is_valid():
			title = request.POST['title']
			link = request.POST['link']

			current_user = request.user
			upload=Paper(title=title, author=current_user, link=link)
			upload.save()
	return render(request, 'testdb/paper_form.html')


def search_focal(request):

	template = 'testdb/focal.html'

	datef = request.GET.get('datef')
	datet = request.GET.get('datet')

	if datef and datet:
		results = Focal.objects.filter(
			Q(date_posted__gte=datef) & Q(date_posted__lte=datet) 
			)
	else:
		results = Focal.objects.all()

	print(results)

	context = {
		'focal': results
	}
	return render(request, template, context)



# def search_posts(request):

# 	template = 'testdb/search.html'

# 	datef = request.GET.get('datef')
# 	datet = request.GET.get('datet')

# 	Magnitudef = request.GET.get('Magnitudef')
# 	Magnitudet = request.GET.get('Magnitudet')

# 	Latitudef = request.GET.get('Latitudef')
# 	Latitudet = request.GET.get('Latitudet')

# 	Longitudef = request.GET.get('Longitudef')
# 	Longitudet = request.GET.get('Longitudet')

# 	Depthf = request.GET.get('Depthf')
# 	Deptht = request.GET.get('Deptht')

# 	search = {
# 		'datef':datef,
# 		'datet':datet,
# 		'Latitudef':Latitudef,
# 		'Latitudet':Latitudet,
# 		'Longitudef':Longitudef,
# 		'Longitudet':Longitudet,
# 	}

# 	search1 = {
# 		'Magnitudef':Magnitudef,
# 		'Magnitudet':Magnitudef,
# 		'Depthf':Depthf,
# 		'Deptht':Deptht
# 	}


# 	if search:
# 		results = Post.objects.filter(
# 			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
# 			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
# 			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
# 			)

# 	elif search1:
# 		results = Post.objects.filter(
# 			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
# 			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
# 			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
# 			& Q(Magnitude__gte=Magnitudef), Q(Magnitude__lte=Magnitudet)
# 			& Q(Depth__gte=Depthf), Q(Depth__lte=Deptht)
# 			)




# 	elif Magnitudef and Magnitudet:
# 		results = Post.objects.filter(
# 			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
# 			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
# 			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
# 			& Q(Magnitude__gte=Magnitudef), Q(Magnitude__lte=Magnitudet)
# 			)

# 	elif Depthf and Deptht:
# 		results = Post.objects.filter(
# 			Q(date_posted__gte=datef), Q (date_posted__lte=datet)
# 			& Q(Latitude__gte=Latitudef), Q(Latitude__lte=Latitudet)
# 			& Q(Longitude__gte=Longitudef), Q(Longitude__lte=Longitudet)
# 			& Q(Depth__gte=Depthf), Q(Depth__lte=Deptht)
# 			)


# 	else:
# 		results = Post.objects.all()

# 	context = {
#         'posts': results
#     }

# 	return render(request, template, context)


from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search_results(request):
    queryset = Post.objects.all()

    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    latitude_min = request.GET.get('latitude_min')
    latitude_max = request.GET.get('latitude_max')
    longitude_min = request.GET.get('longitude_min')
    longitude_max = request.GET.get('longitude_max')
    depth_min = request.GET.get('depth_min')
    depth_max = request.GET.get('depth_max')
    magnitude_min = request.GET.get('magnitude_min')
    magnitude_max = request.GET.get('magnitude_max')
    magnitudemw_min = request.GET.get('magnitudemw_min')
    magnitudemw_max = request.GET.get('magnitudemw_max')

    if date_from and date_to:
        queryset = queryset.filter(Q(date_posted__range=[date_from, date_to]))

    if latitude_min and latitude_max:
        queryset = queryset.filter(Q(Latitude__range=[latitude_min, latitude_max]))

    if longitude_min and longitude_max:
        queryset = queryset.filter(Q(Longitude__range=[longitude_min, longitude_max]))

    if depth_min and depth_max:
        queryset = queryset.filter(Q(Depth__range=[depth_min, depth_max]))

    if magnitude_min and magnitude_max:
        queryset = queryset.filter(Q(Magnitude__range=[magnitude_min, magnitude_max]))

    if magnitudemw_min and magnitudemw_max:
        queryset = queryset.filter(Q(Magnitudemw__range=[magnitudemw_min, magnitudemw_max]))

    return render(request, 'testdb/search_results.html', {'results': queryset})




def home(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request, 'testdb/home.html', context)


def search(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request, 'testdb/search.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'testdb/home.html'
	context_object_name = 'posts'
	paginate_by = 10


class PostListView3(ListView):
	model = Post
	template_name = 'testdb/search.html'
	context_object_name = 'posts'
	paginate_by = 10

class UserPostListView(ListView):
	model = Post
	template_name = 'testdb/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
	model = Post
	template_name = 'testdb/post_detail.html'




class PostDetailView2(DetailView):
	model = Post
	template_name = 'testdb/post_phase.html'


class MagValueView(DetailView):
	model = Post
	template_name = 'testdb/mag_value.html'



def focal(request):
	context = {
        'focal': Focal.objects.all()
    }
	return render(request, 'testdb/focal.html', context, {'title': 'Focal Mechanism'})



class PostListView2(ListView):
	model = Focal
	template_name = 'testdb/focal.html'
	context_object_name = 'focal'
	paginate_by = 10

class PostListView4(ListView):
	model = Report
	template_name = 'testdb/report.html'
	context_object_name = 'report'
	paginate_by = 5

class PostListView5(ListView):
	model = Paper
	template_name = 'testdb/paper.html'
	context_object_name = 'paper'
	paginate_by = 5

class PostListView6(ListView):
	model = stations
	template_name = 'testdb/Seismic.html'
	context_object_name = 'stations'
	paginate_by = 5

# class PostCreateView(LoginRequiredMixin, CreateView):
# 	model = Post
# 	fields = ['image', 'Region']

# CreateView
	

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = [
    'RMS',
    'lu1',
    'lu2',
    'Latitude',
    'Longitude',
    'Depth',
    'event',
    'Gap',
    'Magnitude',
    'MagnitudeMw',
    'Region',
    'image',
    'image2',
    'station',
    'comp',
    'DIS',
    'AZM',
    'ARR_TIME',
    'RES',
    'PHASE',
    'date_posted',
    'station_m',
    'comp_m',
    'DIS_m',
    'azm_m',
    'b_azm_m',
    'amp_m',
    'gain_m',
    'local_m_m',
    'station_m2',
    'comp_m2',
    'DIS_m2',
    'azm_m2',
    'b_azm_m2',
    'amp_m2',
    'gain_m2',
    'local_m_m2']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



def about(request):
    return render(request, 'testdb/about.html', {'title': 'About'})

def publications(request):
    return render(request, 'testdb/publications.html', {'title': 'Publications'})

def seismic(request):
    return render(request, 'testdb/Seismic.html', {'title': 'Seismic'})

