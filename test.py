from fpdf import FPDF

class PDF(FPDF):
    # def header(self):
    #     self.image('header.png', 10, 8, 190)  # Add a header image
    #     self.set_font('Arial', 'B', 12)
    #     self.cell(0, 10, 'Appointment Details', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_fill_color(200, 200, 200)  # Gray background color
        self.cell(0, 12, title, 0, 1, 'L')
        self.ln(10)

    # def chapter_field(self, title, value):
    #     self.set_font('Arial', 'B', 12)
    #     self.cell(70, 10, title, 0)
    #     self.set_font('Arial', '', 12)
    #     self.cell(0, 10, value)
    #     self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_invoice(patient_name, appointment_number, payment_status, total_amount, payment_id, hospital_name, doctor_name, gender, appointment_date, appointment_schedule, phone_number, patient_age):
    pdf = PDF()
    pdf.add_page()

    # Title
    pdf.chapter_title('Invoice')

    # Customer name and invoice number
    pdf.chapter_title('Patient Name:'+ patient_name)
    pdf.chapter_title('Invoice Number:' + payment_status)
    pdf.chapter_title('Appointment Number:'+ appointment_number)
    pdf.chapter_title('Payment ID:'+str(payment_id))
    pdf.chapter_title('Hospital Name:'+ hospital_name)
    pdf.chapter_title('Doctor Name:'+ doctor_name)
    pdf.chapter_title('Gender:'+ gender)
    pdf.chapter_title('Appointment Date:'+ appointment_date)
    pdf.chapter_title('Appointment Schedule:'+ appointment_schedule)
    pdf.chapter_title('Phone Number:'+ str(phone_number))
    pdf.chapter_title('Patient Age:'+ str(patient_age))
    pdf.ln(5)

    # Total amount
    pdf.chapter_title(f'Total Amount: ${total_amount:.2f}')
    name = "yash"

    # Output to a PDF file
    pdf.output(f"{name}_appointment.pdf")

if __name__ == '__main__':
    patient_name = "John Doe"
    appointment_number = "INV12345"
    payment_status = "successful"
    total_amount = 35
    payment_id = 1531
    hospital_name = "Jantaram"
    doctor_name = "Lahane"
    gender = "Male"
    appointment_date = "10/04/2004"
    appointment_schedule = "11pm"
    phone_number = 9881967037
    patient_age = 19

    create_invoice(patient_name, appointment_number, payment_status, total_amount, payment_id, hospital_name, doctor_name, gender, appointment_date, appointment_schedule, phone_number, patient_age)
