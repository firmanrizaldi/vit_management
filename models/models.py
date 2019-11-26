from odoo import models, fields, api
import time

class PerangkatDC(models.Model):
    _name = 'management.perangkat'
    _rec_name = 'no_reg'


    
    pemilik = fields.Char(
        string='Pemilik',  
    )

    ruang_id = fields.Many2one(
        string='Ruang/Posisi',
        comodel_name='management.ruang',
        ondelete='restrict',
    )
    
    no_reg = fields.Char(
        string='No.Reg',
        readonly=True 
        
    )

    merek_id = fields.Many2one(
        string='Merek/Model/Tipe',
        comodel_name='management.merek',
        ondelete='restrict',
    )
    
    spesifikasi = fields.Char(
        string='Spesifikasi',
    )

    fungsi = fields.Char(
        string='Fungsi',
    )

    visit = fields.Integer(
        string='Visit',
    )
    
    note = fields.Text(
        string='Note',
    )

    @api.model
    def create(self, vals):
        if not vals.get('no_reg', False) or vals['no_reg'] == 'New':
            vals['no_reg'] = self.env['ir.sequence'].next_by_code('management.perangkat') or 'Error Number!!!'
        return super(PerangkatDC, self).create(vals)



class Maintenances(models.Model):
    _name = 'management.maintenances'
    _rec_name = 'date'
    
    date = fields.Date(
        string="Start Date",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

    tiket = fields.Char(
        string='Tiket',
        required=True  
    )

    tujuan = fields.Char(
        string='Tujuan',
        required=True  
    )
    
    status = fields.Text(
        string='Status',
    )

class PowerDistribution(models.Model):
    _name = 'management.power'
    _rec_name = 'ruang_id'


    ruang_id = fields.Many2one(
        string='Ruang/Posisi',
        comodel_name='management.ruang',
        ondelete='restrict',
    )

    
    capacity_id = fields.Many2one(
        string='Posisi',
        comodel_name='management.capacity',
        ondelete='restrict',
    )
    

    no_reg = fields.Char(
        string='No.Reg',
        required=True  
    )

    merek_id = fields.Many2one(
        string='Merek/Model/Tipe',
        comodel_name='management.merek',
        ondelete='restrict',
    )

    fungsi = fields.Char(
        string='Fungsi',
        required=True  
    )

    koneksi_listrik = fields.Char(
        string='Koneksi Listrik',
        required=True  
    )

    distribusi = fields.Integer(
        string='Distribusi',
        required=True  
    )

    visit = fields.Integer(
        string='Visit',
        required=True  
    )

    note = fields.Text(
        string='Note',
    )

class Capacity(models.Model):
    _name = 'management.capacity'
    _rec_name = 'rack'

    
    rack = fields.Char(
        string='Rack',
        required=True
    )

    used = fields.Integer(
        string='Used',
        required=True
    )

    available = fields.Integer(
        string='Available',
        required=True
    )

class PerangkatDcUtilasi(models.Model):
    _name = 'management.perangkatutilasi'
    _rec_name = 'OS'

    
    OS = fields.Char(
        string='OS',
        required=True,
    )

    cpu = fields.Char(
        string='CPU',
        required=True,
    )

    ram = fields.Char(
        string='RAM',
        required=True,
    )

    disk = fields.Char(
        string='Disk',
        required=True,
    )

    
    traffic= fields.Float(
        string='Traffic In/Out',
        required=True,
    )
    
    fungsi = fields.Char(
        string='Fungsi/Note',
        required=True,
    )

class Rekruitment(models.Model):
    _name = 'management.rekruitmen'
    _rec_name = 'name'
    
    
    name = fields.Char(
        string='name',
        required=True
    )
    
    kode = fields.Char(
        string='Kode',
        required=True
    )

    
    kelamin = fields.Selection(
        string='Kelamin',
        selection=[
            ('L', 'Pria'), 
            ('P', 'Wanita')],
        default='L'
    )
    

    usia = fields.Integer(
        string='Usia',
        required=True
    )
    
    pendidikan = fields.Char(
        string='Pendidikan',
        required=True
    )
    Telp = fields.Integer(
        string='Telp',
        required=True
    )

    email = fields.Char(
        string='Email',
        required=True
    )

    file = fields.Char(
        string='File',
        required=True
    )

    pengalaman = fields.Selection(
        string='Pengalaman',
        selection=[
            ('Y', 'Yes'), 
            ('N', 'No')],
        default='N'
    )

    catatan = fields.Text(
        string='Catatan',
    )
    
class Sop(models.Model):
    _name="management.sop" 
    _rec_name = 'code'  

    
    code = fields.Char(
        string='Code', 
        required=True
    )

    sop_name = fields.Char(
        string='SOP Name', 
        required=True
    )

    date_issued = fields.Date(
        string="Date Issued",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

    date_review = fields.Date(
        string="Date Review",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

    date_revised = fields.Date(
        string="Date Revised",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

class Bcp(models.Model):
    _name="management.bcp" 
    _rec_name = 'code'  

    
    code = fields.Char(
        string='Code', 
        required=True
    )

    bcp_name = fields.Char(
        string='BCP Name', 
        required=True
    )

    date_issued = fields.Date(
        string="Date Issued",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

    date_review = fields.Date(
        string="Date Review",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

    date_revised = fields.Date(
        string="Date Revised",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )
    
class Berita(models.Model):
    _name="management.berita" 
    _rec_name = 'judul'  

    
    judul = fields.Char(
        string='Judul', 
        required=True
    )

    date_posting = fields.Date(
        string="Tgl posting",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

    
    publish = fields.Selection(
        string='Publish',
        selection=[('Y', 'Yes'), ('N', 'No')],
        default='Y'
    )
    
    
class Agenda(models.Model):
    _name="management.agenda" 
    _rec_name = 'tema'  

    
    tema = fields.Char(
        string='Tema', 
        required=True
    )

    tgl_mulai = fields.Date(
        string="Tgl Mulai",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )

    tgl_selesai = fields.Date(
        string="Tgl Selesai",
        required=True, 
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )
    
class Datauser(models.Model):
    _name="management.user" 
    _rec_name = 'username'     

    
    username = fields.Char(
        string='Username',
        required=True
    )

    
    identittas = fields.Integer(
        string='Identittas',
        required=True
    )

    nama_lengkap = fields.Char(
        string='Nama Lengkap',
        required=True
    )

    level = fields.Char(
        string='Level',
        required=True
    )
    
    blokir = fields.Selection(
        string='Blokir',
        selection=[('Y', 'Yes'), ('N', 'No')],
        default='N'
    )
    
    pemandu = fields.Selection(
        string='Pemandu',
        selection=[('Y', 'Yes'), ('N', 'No')],
        default='N'
    )
    
    pengelola = fields.Selection(
        string='Pengelola',
        selection=[('Y', 'Yes'), ('N', 'No')],
        default='N'
    )
    
    temp_admin = fields.Selection(
        string='Temp Admin',
        selection=[('Y', 'Yes'), ('N', 'No')],
        default='N'
    )
    
class Lokasi(models.Model):
    _name="management.lokasi" 
    _rec_name = 'lokasi' 

    
    no_lokasi = fields.Integer(
        string='No Lokasi',
        required=True
    )

    
    lokasi = fields.Char(
        string='Lokasi',
        required=True 
    )
    
class Ruang(models.Model):
    _name="management.ruang" 
    _rec_name = 'nama_ruang'     
    
    
    
    lokasi_id = fields.Many2one(
        string='Lokasi',
        comodel_name='management.lokasi',
        ondelete='restrict',
    )
    

    
    no_ruang = fields.Integer(
        string='No Ruang',
        required=True
    )
    
    nama_ruang = fields.Char(
        string='Nama Ruang',
        required=True
    )

class SubRuang(models.Model):
    _name="management.sub_ruang" 
    _rec_name = 'nama_sub_ruang'     
    
    
    
    ruang_id = fields.Many2one(
        string='Ruang',
        comodel_name='model.name',
        ondelete='restrict',
    )
    

    
    no_sub_ruang = fields.Integer(
        string='No Sub Ruang',
        required=True
    )
    
    nama_sub_ruang = fields.Char(
        string='Nama Sub Ruang',
        required=True
    )

class Merek(models.Model):
    _name="management.merek" 
    _rec_name = 'merk'     
    
    
    merk = fields.Char(
        string='merk',
        required=True
    )


class Unit(models.Model):
    _name="management.unit" 
    _rec_name = 'no_unit'     
    
    
    no_unit = fields.Integer(
        string='No Unit',
        required=True
    )
    
    nama_unit = fields.Char(
        string='Nama Unit',
        required=True
    )
    
class SubUnit(models.Model):
    _name="management.sub_unit" 
    _rec_name = 'nama_sub_unit'     
    
    unit_id = fields.Many2one(
        string='Kode/Golongan Perangkat',
        comodel_name='management.unit',
        ondelete='restrict',
    )
    
    no_sub_unit = fields.Integer(
        string='No Sub Unit',
    )

    nama_sub_unit= fields.Char(
        string='Nama Sub Unit',
    )
       

class KodePerangkat(models.Model):
    _name="management.kode_perangkat" 
    _rec_name = 'golongan_perangkat'   

    
    no_perangkat = fields.Integer(
        string='no_perangkat',
    )

    
    golongan_perangkat = fields.Char(
        string='Golongan Perangkat',
    )
     

class KelompokPerangkat(models.Model):
    _name="management.kelompok_perangkat" 
    _rec_name = 'nama_kelompok_perangkat'     

    
    
    kodeperangkat_id = fields.Many2one(
        string='Golongan Perangkat',
        comodel_name='model.name',
        ondelete='restrict',
    )
    
    
    no_kelompok_perangkat = fields.Integer(
        string='No Kelompok Perangkat',
    )

    
    nama_kelompok_perangkat = fields.Char(
        string='Nama Kelompok Perangkat',
    )
    
    
    
    
    
    
    
    
    
    
    
    
    

    