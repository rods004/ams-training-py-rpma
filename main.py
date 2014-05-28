#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
	template_object = {
		'title' : 'This is the main handler',
		#'image_path' : '../static_content/images/Lighthouse.jpg',
		'element_list' : ['Read python.', 'Finish training.']
	}
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'templates/main_template.html')
		self.response.out.write(template.render(path, self.template_object))

class NewHandler(MainHandler):
	template_object = {
		'title' : 'This is the new handler',
		'element_list' : ['Learn to add images to the template']
	}
	def get(self):
		super(NewHandler, self).get()

class OldHandler(MainHandler):
	template_object = {"title": 'This is the old handler',
		'element_list' : ['Learn to add title to the template']
	}
	def get(self):
		super(OldHandler, self).get()

class BlueHandler(MainHandler):
	template_object = {
		'title' : 'This is the blue handler',
		'element_list' : []
	}
	def get(self):
		super(BlueHandler, self).get()

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/main/', MainHandler),
	('/main/new', NewHandler),
	('/main/old', OldHandler),
	('/main/blue', BlueHandler)
], debug=True)
