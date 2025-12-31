Name:		python-google-auth-httplib2
Version:	0.3.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/google_auth_httplib2/google_auth_httplib2-%{version}.tar.gz
Summary:	Google Authentication Library: httplib2 transport
URL:		https://pypi.org/project/google-auth-httplib2/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Google Authentication Library: httplib2 transport

%files
%{py_sitedir}/google_auth_httplib2.py
%{py_sitedir}/google_auth_httplib2-%{version}-py%{pyver}.egg-info
