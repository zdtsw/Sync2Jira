# This file is part of sync2jira.
# Copyright (C) 2016 Red Hat, Inc.
#
# sync2jira is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# sync2jira is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with sync2jira; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110.15.0 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>

config = {
    # mandatory 
    'sync2jira': {
        # Admins to be cc'd in duplicate emails
        'admins': [{'admin_username': 'wenzhou@redhat.com'}],

        # Mailing list email to send failure-email notices too
        'mailing-list': 'wenzhou@redhat.com',

        # Listen on the message bus
        'listen': True,

        # Don't actually make changes to JIRA...
        'testing': True,

        # Set to True when developing to disable sentinel query
        'develop': False,

        # Your Github token, or we might have rate-limited 5000 per hour
        'github_token': 'GITHUB_API_TOKEN',

        # If we should update a Confluence page for stats
        'confluence_statistics': False,

        'legacy_matching': False,

        # for the very first time, or can just use 'recent' method
        'initialize': True,

        'default_jira_instance': 'issues.redhat.com',
        'jira_username': 'wenzhou',

        # Mandatory
        'jira': {
            'example': {
                'options': {
                    'server': 'https://issues.redhat.com',
                    'verify': True,
                },
                'token_auth': 'JIRA_ACCESS_TOKEN',
            },
        },

        'map': {
            'github': {
                'red-hat-data-services/notebooks': {'project': 'red-hat-data-services', 'component': 'notebooks','updates': [...], 'sync': ['pullrequest']},
                'red-hat-data-services/odh-deployer': {'project': 'red-hat-data-services', 'component': 'odh-deployer','updates': [...], 'sync': ['pullrequest']},
            },
        },

        'filters': {
            'github': {
                # set as upstream
                'red-hat-data-services/notebooks': {'status': 'open', 'milestone': 4, },
            },
        }
    },
}
