# 
# Fist Python Script to split and IPv6 address and join it again. v 2.0
#

ipv6_addr = '1111:2222:3333:4444:5555:6666:7777:8888'

ipv6_sections = ipv6_addr.split(":")

print 
print "IPv6 address split"
print ipv6_sections
print

ipv6_new = ":".join(ipv6_sections)

print "IPv6 address re-joined:"
print
print ipv6_new
print


