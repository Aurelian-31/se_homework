# Dependence Inversion Principle
*依赖倒置原则*（Dependence Inversion Principle，DIP）是 Object Mentor 公司总裁罗伯特·马丁（Robert C.Martin）于 1996 年在 C++ Report 上发表的文章。

依赖倒置原则的原始定义为：

>High level modules shouldnot depend upon low level modules.Both should depend upon abstractions.Abstractions should not depend upon details. Details should depend upon abstractions.

![Dependency Inversion Principle](/dip.png)


* 其核心思想是：要面向接口编程，不要面向实现编程。

**依赖倒置原则是实现开闭原则的重要途径之一，它降低了客户与实现模块之间的耦合**。

由于在软件设计中，细节具有多变性，而抽象层则相对稳定，因此以抽象为基础搭建起来的架构要比以细节为基础搭建起来的架构要稳定得多。这里的抽象指的是接口或者抽象类，而细节是指具体的实现类。

使用接口或者抽象类的目的是制定好规范和契约，而不去涉及任何具体的操作，把展现细节的任务交给它们的实现类去完成。
## 依赖、倒置原则的作用
依赖倒置原则的主要作用如下:
1. 依赖倒置原则可以降低类间的耦合性。
2. 依赖倒置原则可以提高系统的稳定性。
3. 依赖倒置原则可以减少并行开发引起的风险。
4. 依赖倒置原则可以提高代码的可读性和可维护性。

## 依赖倒置原则的实现方法
依赖倒置原则的目的是通过要面向接口的编程来降低类间的耦合性，所以我们在实际编程中只要遵循以下4点，就能在项目中满足这个规则:
1. 每个类尽量提供接口或抽象类，或者两者都具备。
2. 变量的声明类型尽量是接口或者是抽象类。
3. 任何类都不应该从具体类派生。
4. 使用继承时尽量遵循里氏替换原则。

下面以“顾客购物程序”为例来说明依赖倒置原则的应用。

**例1** 依赖倒置原则在“顾客购物程序”中的应用。
本程序反映了 “顾客类”与“商店类”的关系。商店类中有 sell() 方法，顾客类通过该方法购物以下代码定义了顾客类通过网店 SWUFEShop 购物

    class Customer {
        public void shopping(SWUFEShop shop) {
            //购物
            System.out.println(shop.sell());
        }
    }
    
但是，这种设计存在缺点，如果该顾客想从另外一家商店（如网店 PKUShop）购物，就要将该顾客的代码修改如下：

    class Customer {
    public void shopping(PKUShop shop) {
        //购物
        System.out.println(shop.sell());
    }
}

顾客每更换一家商店，都要修改一次代码，这明显违背了开闭原则。存在以上缺点的原因是：顾客类设计时同具体的商店类绑定了，这违背了依赖倒置原则。解决方法是：定义“SWUFE网店”和“PKU网店”的共同接口 Shop，顾客类面向该接口编程，其代码修改如下：

    class Customer {
    public void shopping(Shop shop) {
        //购物
        System.out.println(shop.sell());
    }
}
这样，不管顾客类 Customer 访问什么商店，或者增加新的商店，都不需要修改原有代码了
