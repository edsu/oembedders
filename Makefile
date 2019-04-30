all: download copy cleanup

download:
	wget https://github.com/iamcal/oembed/archive/master.zip
	rm -rf oembed-master
	unzip master.zip

copy:
	cp -r oembed-master/providers oembedders/

cleanup:
	rm master.zip
	rm -rf oembed-master
