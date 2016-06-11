# coding: utf-8
from subDomainsBrute import DNSBrute
import re
import os
import threading
import time


def get_sub_domain_ip_map(
        target,
        save_tmp_file=True,
        names_file="dict/subnames_largest.txt",
        ignore_intranet=False,
        threads_num=60,
        output=None):
    d = DNSBrute(
            target=target,
            names_file=names_file,
            ignore_intranet=ignore_intranet,
            threads_num=threads_num,
            output=output)
    d.run()
    while threading.activeCount() > 1:
        time.sleep(0.1)
    time.sleep(1)
    outfile = target + '.txt' if not output else output
    res = {}
    with open(outfile,'r') as f:
        for line in f:
            domain, ips = re.split(r' *', line, 1)
            ips = ips.split(',')
            res[domain] = [ip.strip() for ip in ips]
    if not save_tmp_file:
        os.popen('rm %s' % outfile)
    return res


if __name__ == "__main__":
    print get_sub_domain_ip_map(
            "qiushibaike.com",
            True,
            "dict/test_subnames.txt")
