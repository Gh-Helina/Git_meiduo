
def get_breadcrumb(category):
    # 分类为三级
    # 返回字典记录三个分类
    breadcrumb={
        'cat1':'',
        'cat2' : '',
        'cat3' : ''
    }
    # 根据当前传递过来的分类进行判断
    if category.parent is None:
        #一级标题
        breadcrumb['cat1']=category
    elif category.subs.count()==0:
        # 说明下边没有分类,是三级
        breadcrumb['cat3']=category
        breadcrumb['cat2']=category.parent
        breadcrumb['cat1']= category.parent.parent
    else:
        # 二级
        breadcrumb['cat2']=category
        breadcrumb['cat1']=category.parent
    return breadcrumb



import os
from django.template import loader
from django.conf import settings
from apps.goods import models
from apps.contents.utils import get_categories


def get_detail_html(sku_id):
    """
        生成静态商品详情页面
        :param sku_id: 商品sku id
        """
    # 获取当前sku的信息
    sku = models.SKU.objects.get(id=sku_id)

    # 查询商品频道分类
    categories = get_categories()
    # 查询面包屑导航
    breadcrumb = get_breadcrumb(sku.category)

    # 构建当前商品的规格键
    sku_specs = sku.specs.order_by('spec_id')
    sku_key = []
    for spec in sku_specs:
        sku_key.append(spec.option.id)
    # 获取当前商品的所有SKU
    skus = sku.spu.sku_set.all()
    # 构建不同规格参数（选项）的sku字典
    spec_sku_map = {}
    for s in skus:
        # 获取sku的规格参数
        s_specs = s.specs.order_by('spec_id')
        # 用于形成规格参数-sku字典的键
        key = []
        for spec in s_specs:
            key.append(spec.option.id)
        # 向规格参数-sku字典添加记录
        spec_sku_map[tuple(key)] = s.id
    # 获取当前商品的规格信息
    goods_specs = sku.spu.specs.order_by('id')
    # 若当前sku的规格信息不完整，则不再继续
    if len(sku_key) < len(goods_specs):
        return
    for index, spec in enumerate(goods_specs):
        # 复制当前sku的规格键
        key = sku_key[:]
        # 该规格的选项
        spec_options = spec.options.all()
        for option in spec_options:
            # 在规格参数sku字典中查找符合当前规格的sku
            key[index] = option.id
            option.sku_id = spec_sku_map.get(tuple(key))
        spec.spec_options = spec_options

    # 上下文
    context = {
        'categories': categories,
        'breadcrumb': breadcrumb,
        'sku': sku,
        'specs': goods_specs,
    }

    template = loader.get_template('detail.html')
    html_text = template.render(context)
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'detail/' + str(sku_id) + '.html')
    with open(file_path, 'w') as f:
        f.write(html_text)