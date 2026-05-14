import os
import django
import urllib.request
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_system.settings')
django.setup()

from hospital.models import Department, Doctor

def populate():
    cardio, _ = Department.objects.get_or_create(name='Cardiology', description='Advanced heart care.', icon='fa-heartbeat')
    neuro, _ = Department.objects.get_or_create(name='Neurology', description='Expert care for brain and nervous system.', icon='fa-brain')
    ortho, _ = Department.objects.get_or_create(name='Orthopedics', description='Care for bones and joints.', icon='fa-bone')
    pedia, _ = Department.objects.get_or_create(name='Pediatrics', description='Dedicated care for infants and children.', icon='fa-baby')
    
    doctors_data = [
        {
            'name': 'Sarah Jenkins',
            'department': cardio,
            'experience': 15,
            'qualification': 'MD, FACC, Board Certified Cardiologist',
            'available_days': 'Mon, Wed, Fri (9 AM - 2 PM)',
            'consultation_fee': 150.00,
            'image_url': 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80&w=600'
        },
        {
            'name': 'Michael Chen',
            'department': neuro,
            'experience': 12,
            'qualification': 'MD, PhD in Neurology',
            'available_days': 'Tue, Thu (10 AM - 4 PM)',
            'consultation_fee': 200.00,
            'image_url': 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&q=80&w=600'
        },
        {
            'name': 'Emily Rodriguez',
            'department': pedia,
            'experience': 8,
            'qualification': 'MD, FAAP',
            'available_days': 'Mon to Fri (8 AM - 12 PM)',
            'consultation_fee': 100.00,
            'image_url': 'https://images.unsplash.com/photo-1594824436998-dd40e4f6918a?auto=format&fit=crop&q=80&w=600'
        },
        {
            'name': 'David Smith',
            'department': ortho,
            'experience': 20,
            'qualification': 'MD, Orthopedic Surgeon',
            'available_days': 'Wed, Fri, Sat (1 PM - 6 PM)',
            'consultation_fee': 180.00,
            'image_url': 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&q=80&w=600'
        },
        {
            'name': 'Jessica Wong',
            'department': cardio,
            'experience': 10,
            'qualification': 'MD, Pediatric Cardiologist',
            'available_days': 'Tue, Thu, Sat (9 AM - 1 PM)',
            'consultation_fee': 160.00,
            'image_url': 'https://images.unsplash.com/photo-1614608682850-e0d6ed316d47?auto=format&fit=crop&q=80&w=600'
        }
    ]

    for data in doctors_data:
        doc, created = Doctor.objects.get_or_create(
            name=data['name'],
            defaults={
                'department': data['department'],
                'experience': data['experience'],
                'qualification': data['qualification'],
                'available_days': data['available_days'],
                'consultation_fee': data['consultation_fee'],
                'is_active': True
            }
        )
        if created or not doc.image:
            print(f"Downloading image for {doc.name}...")
            req = urllib.request.Request(data['image_url'], headers={'User-Agent': 'Mozilla/5.0'})
            try:
                with urllib.request.urlopen(req) as response:
                    img_data = response.read()
                    file_name = f"{data['name'].replace(' ', '_').lower()}.jpg"
                    doc.image.save(file_name, ContentFile(img_data), save=True)
                    print(f"Saved image for {doc.name}")
            except Exception as e:
                print(f"Failed to download image for {doc.name}: {e}")

if __name__ == '__main__':
    print("Populating database with doctors...")
    populate()
    print("Done!")
