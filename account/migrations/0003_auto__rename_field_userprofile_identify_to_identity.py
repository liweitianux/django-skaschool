# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Rename field 'identify' to 'identity'
        db.rename_column(u'account_userprofile', 'identify', 'identity')


    def backwards(self, orm):
        # Rename field 'identity' to 'identify'
        db.rename_column(u'account_userprofile', 'identity', 'identify')


    models = {
        u'account.userfile': {
            'Meta': {'ordering': "['user', 'id']", 'object_name': 'UserFile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('account.extra.ContentTypeRestrictedFileField', [], {'content_types': "['application/gzip', 'application/msword', 'application/pdf', 'application/postscript', 'application/rar', 'application/vnd.ms-excel', 'application/vnd.oasis.opendocument.spreadsheet', 'application/vnd.oasis.opendocument.text', 'application/vnd.oasis.opendocument.presentation', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/wps-office.doc', 'application/wps-office.dps', 'application/wps-office.et', 'application/wps-office.ppt', 'application/wps-office.pptx', 'application/wps-office.wps', 'application/wps-office.xls', 'application/zip', 'application/x-7z-compressed', 'application/x-bzip2', 'application/x-dvi', 'application/x-latex', 'application/x-rar-compressed', 'application/x-tar', 'image/bmp', 'image/gif', 'image/jpeg', 'image/png', 'image/tiff', 'text/csv', 'text/plain', 'text/rtf', 'text/x-markdown', 'text/x-tex']", 'max_upload_size': '10485760', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'institute': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'is_approved': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'is_checkin': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '1'}),
            'is_sponsored': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'realname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'supplement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'transcript': ('account.extra.ContentTypeRestrictedFileField', [], {'content_types': "['application/gzip', 'application/msword', 'application/pdf', 'application/postscript', 'application/rar', 'application/vnd.ms-excel', 'application/vnd.oasis.opendocument.spreadsheet', 'application/vnd.oasis.opendocument.text', 'application/vnd.oasis.opendocument.presentation', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/wps-office.doc', 'application/wps-office.dps', 'application/wps-office.et', 'application/wps-office.ppt', 'application/wps-office.pptx', 'application/wps-office.wps', 'application/wps-office.xls', 'application/zip', 'application/x-7z-compressed', 'application/x-bzip2', 'application/x-dvi', 'application/x-latex', 'application/x-rar-compressed', 'application/x-tar', 'image/bmp', 'image/gif', 'image/jpeg', 'image/png', 'image/tiff', 'text/csv', 'text/plain', 'text/rtf', 'text/x-markdown', 'text/x-tex']", 'max_upload_size': '10485760', 'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['account']
