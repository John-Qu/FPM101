import os
import glob
import yaml

def read_yaml_files(path):
    files = glob.glob(os.path.join(path, '*.yml'))
    data = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            data.append(yaml.safe_load(fh))
    return data

def as_text(v):
    if v is None:
        return 'tbd'
    if isinstance(v, list):
        return ', '.join([str(x) for x in v]) if v else 'tbd'
    return str(v)

def build_table(rows):
    headers = ['品牌', '系列', '机型', '包装形式', '道数', '托盘/分', '残氧', '泄漏率', '换型时间', '材料', '控制', '创新亮点']
    lines = []
    lines.append('| ' + ' | '.join(headers) + ' |')
    lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
    for r in rows:
        line = [
            as_text(r.get('brand')),
            as_text(r.get('series')),
            as_text(r.get('model')),
            as_text(r.get('packaging')),
            as_text(r.get('lanes')),
            as_text(r.get('throughput_trays_per_min')),
            as_text(r.get('residual_o2_target')),
            as_text(r.get('leak_rate_target')),
            as_text(r.get('tool_change_time_min')),
            as_text(r.get('materials')),
            as_text(r.get('controls')),
            as_text(r.get('auth_innovations')),
        ]
        lines.append('| ' + ' | '.join(line) + ' |')
    return '\n'.join(lines)

def main():
    data = read_yaml_files('data/competitors')
    table_md = build_table(data)
    out_path = os.path.join('docs', 'competitors', 'overview.md')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write('# 竞品总览对比\n\n')
        fh.write(table_md + '\n')
        fh.write('\n来源详见各机型档案与数据文件。\n')

if __name__ == '__main__':
    main()