# MONGO DATABASE SETTINGS
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'keystone'

# ALLOW ACTIONS
DEBUG = False
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE'] if DEBUG else ['GET']

bookmark_schema = {
  'slug': {
    'type': 'string',
  },
  'style': {
    'type': 'string',
  },
  'bookmark': {
    'type': 'string',
  },
  'bookmark_order': {
    'type': 'number',
  }
}

meta_schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'topics': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'topics',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'style': {
    'type': 'string',
  },
  'bookmark': {
    'type': 'string',
  },
  'tags': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'tags',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'publishedDate': {
    'type': 'string',
  },
  'og_description': {
    'type': 'string',
  },
}

post_schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'leading_video': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImageSize': {
    'type': 'string',
  }, 
  'state': {
    'type': 'string',
  },
  'writters': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'photographers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'designers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'engineers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'publishedDate': {
    'type': 'string',
  },
  'updatedAt': {
    'type': 'string',
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'topics': {
    'type': 'string',
  },
  'tags': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'tags',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'style': {
    'type': 'string',
  },
  'bookmark': {
    'type': 'string',
  },
  'bookmark_order': {
    'type': 'number',
  },
  'related_bookmarks': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'bookmarks',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'content': {
    'type': 'dict',
    'schema': {
       "html": {
          "type": "string",
       },
     },  
  },
  'relateds': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
  'extend_byline': {
    'type': 'string',
  },
  'copyright': {
    'type': 'string',
  },
  'og_title': {
    'type': 'string',
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  }
}

user_schema = {
  'name': {
    'type': 'string',
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
  },
  'role': {
    'type': 'string',
  },
  'company': {
    'type': 'string',
  },
  'address': {
    'type': 'string',
  }
}

contact_schema = {
  'name': {
    'type': 'string',
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  },
  'homepage': {
    'type': 'string',
  },
  'facebook': {
    'type': 'string',
  },
  'twitter': {
    'type': 'string',
  },
  'instantgram': {
    'type': 'string',
  },
  'bio': {
    'type': 'string',
  },
  'image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
}

member_schema = {
  'member_id': {
    'type': 'string',
    'required': True,
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
  },
  'password': {
    'type': 'string',
    'required': True,
  },
  'country': {
    'type': 'string',
  },
  'city': {
    'type': 'string',
  },
  'address': {
    'type': 'string',
  },
  'zip': {
    'type': 'interger',
  },
  'gender': {
    'type': 'string',
  },
  'state': {
      'type': 'dict',
      'schema': {
          'bookmark': {
            'type': 'list',
            'schema': {
              'type': 'objectid',
              'data_relation': {
                'resource': 'posts',
                'field': '_id',
                'embeddabole': True
              },
            },
          },
          'bookmark_count': {
            'type': 'integer',
          },
          'position': {
            'type': 'string',
          }
      },
  },
  'create_date': {
    'type': 'datetime',
  }
}

account_schema = {
    'username': {
       'type': 'string',
       'required': True,
       'unique': True,
    },
    'password': {
       'type': 'string',
       'required': True,
    },
    'roles': {
        'type': 'list',
        'allowed': ['user', 'superuser', 'admin'],
        'required': True,
    },
    'token': {
        'type': 'string',
        'required': True,
    }
}

audios_schema = {
  'description': {
    'type': 'string',
  },
  'audio': {
    'type': 'dict',
    'schema': {
        'filetype': {
          'type': 'string',
        },
        'filename': {
          'type': 'string',
        },
        'originalname': {
          'type': 'string',
        },
        'path': {
          'type': 'string',
        },
        'projectId': {
          'type': 'string',
        },
        'size': {
          'type': 'string',
        },
        'url': {
          'type': 'string',
        },
    },
  },  
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
  'photographer': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'contacts',
      'field': '_id',
      'embeddable': True
    },
  },
}

video_schema = {
  'title': {
    'type': 'string',
  },
  'video': {
    'type': 'dict',
    'schema': {
        'size': {
          'type': 'string',
        },
        'url': {
          'type': 'string',
        },
    },
  },  
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  }
}

topics_schema = {
  'name': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'headline': {
    'type': 'string',
  },
  'state': {
    'type': 'string',
  },
  'description': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'team_description': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'relateds': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
  'publishedDate': {
    'type': 'string',
  },
  'leading_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'leading_image_portrait': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'leading_video': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
}

image_schema = {
  'photographer': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'contacts',
      'field': '_id',
      'embeddable': True
    },
  },
  'description': {
    'type': 'string',
  },
  'sale': {
    'type': 'Boolean',
  },
  'copyright': {
    'type': 'string',
  },
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
  'image': {
    'type': 'dict',
    'schema': {
      'artist': {
        'type': 'string',
      },
      'description': {
        'type': 'string',
      },
      'filename': {
        'type': 'string',
      },
      'filetype': {
        'type': 'string',
      },
      'height': {
        'type': 'number',
      },
      'width': {
        'type': 'number',
      },
      'size': {
        'type': 'number',
      },
      'url': {
        'type': 'string',
      }
    },
  },
}

posts = {
    'item_title': 'post',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['writters','photographers','designers','engineers','heroImage', 'topics', 'related_bookmarks', 'leading_video', 'og_image', 'tags', 'categories'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': post_schema
}

bookmarks = {
    'item_title': 'bookmark',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': [],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': bookmark_schema
}

meta = {
    'item_title': 'draft',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage', 'categories', 'tags' ],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': meta_schema
}

drafts = {
    'item_title': 'draft',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'draft'},
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': post_schema
}

users = {
    'item_title': 'user',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=60,must-revalidate',
    'cache_expires': 60,
    'allow_unknown': False,
    'schema': user_schema
}

members = {
    'item_title': 'member',
    'additional_lookup': {
        'url': 'regex("\w+")',
        'field': 'member_id'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=60,must-revalidate',
    'cache_expires': 60,
    'allow_unknown': False,
    'schema': member_schema
}

contacts = {
    'item_title': 'contact',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': True,
    'embedded_fields': ['image'],
    'schema': contact_schema
}

topics = {
    'item_title': 'topic',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=3600,must-revalidate',
    'cache_expires': 3600,
    'embedded_fields': ['leading_image','leading_image_portrait','leading_video'],
    'allow_unknown': True,
    'schema': topics_schema
}

tags = {
    'item_title': 'tag',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=3600,must-revalidate',
    'cache_expires': 3600,
    'allow_unknown': True,
    'schema': {
      'name': {
        'type': 'string',
      }
    }
}

postcategories = {
    'item_title': 'postcategory',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=3600,must-revalidate',
    'cache_expires': 3600,
    'allow_unknown': True,
    'schema': {
      'name': {
        'type': 'string',
      }
    }
}

account = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },
    'resource_methods': ['GET', 'POST'],
    'allowed_roles': ['superuser', 'admin'],
    'cache_control': '',
    'cache_expires': 0,
    'schema': account_schema,
}

images = {
    'resource_methods': ['GET'],
    'cache_control': 'max-age=3600,must-revalidate',
    'cache_expires': 3600,
    'allow_unknown': False,
    'schema': image_schema,
}

audios = {
    'resource_methods': ['GET'],
    'cache_control': 'max-age=3600,must-revalidate',
    'cache_expires': 3600,
    'allow_unknown': False,
    'schema': audios_schema,
}

videos = {
    'resource_methods': ['GET'],
    'cache_control': 'max-age=3600,must-revalidate',
    'cache_expires': 3600,
    'allow_unknown': False,
    'schema': video_schema,
}

DOMAIN = {
    'bookmarks': bookmarks,
    'posts': posts,
    'drafts': drafts,
    'meta': meta,
    'users': users,
    'members': members,
    'contacts': contacts,
    'tags': tags,
    'topics': topics,
    'postcategories': postcategories,
    'account': account,
    'images': images,
    'audios': audios,
    'videos': videos
  }

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
