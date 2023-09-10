import numpy as np
from manim import *

class DirectedWeightedGraph(Scene):
    def construct(self):
        self.makeGraph()
        self.wait(3)
        self.startPrims()

    def startPrims(self):
        self.group.scale(0.6)
        self.play(self.group.animate.shift(4.5*LEFT))
        #self.wait(3)
        ellipse1 = Ellipse(
            width=3.0, height=5.0 ,stroke_width=7
        ).move_to(LEFT)
        ellipse1.set_color(color=WHITE)
        ellipse2 = ellipse1.copy().set_color(color=WHITE).move_to(3*RIGHT)
        ellipse_group = Group( ellipse1, ellipse2).move_to(RIGHT * 3)
        self.play(FadeIn(ellipse_group))
        #self.wait(3)
        node_S = Dot(point=np.array([1, 2, 0]))
        node_A = Dot(point=np.array([4, 1, 0]))
        node_C = Dot(point=np.array([4, -1, 0]))
        node_D = Dot(point=np.array([5, 2, 0]))
        node_B = Dot(point=np.array([6, 1, 0]))
        node_E = Dot(point=np.array([6, -1, 0]))
        node_T = Dot(point=np.array([5, -2, 0]))

        wnode1 = Tex("S", color=WHITE, font_size=20).next_to(node_S, LEFT)
        wnode2 = Tex("A", color=WHITE, font_size=20).next_to(node_A, UP)
        wnode3 = Tex("B", color=WHITE, font_size=20).next_to(node_B, DOWN)
        wnode4 = Tex("C", color=WHITE, font_size=20).next_to(node_C, UP)
        wnode5 = Tex("D", color=WHITE, font_size=20).next_to(node_D, UP)
        wnode6 = Tex("E", color=WHITE, font_size=20).next_to(node_E, DOWN)
        wnode7 = Tex("T", color=WHITE, font_size=20).next_to(node_T, RIGHT)
        node_group=Group(node_S,node_B,node_C,node_A,node_D,node_E,node_T,wnode1,wnode2,wnode3,wnode4,wnode5,wnode6,wnode7)
        self.play(FadeIn(node_group))
        self.wait(1)
        self.play(node_A.animate.shift(4*LEFT),wnode2.animate.shift(4*LEFT+0.2*DOWN))
        edge1 = Arrow(node_S, node_A,stroke_width=3,max_tip_length_to_length_ratio=0.1, buff=0.05)
        self.play(Create(edge1))
        self.edge1.set_color(color=GREEN)
        self.wait(1)
        self.play(node_D.animate.shift(5 * LEFT+2*DOWN), wnode5.animate.shift(4.75 * LEFT+2.3*DOWN))
        edge2 = Arrow(node_A, node_D, stroke_width=3, max_tip_length_to_length_ratio=0.1, buff=0.05)
        self.play(Create(edge2))
        self.edge4.set_color(color=GREEN)
        self.wait(1)
        self.play(node_B.animate.shift(6 * LEFT + 2 * DOWN), wnode3.animate.shift(6 * LEFT + 1.8 * DOWN))
        edge3 = Arrow(node_D, node_B, stroke_width=3, max_tip_length_to_length_ratio=0.1, buff=0.05)
        self.play(Create(edge3))
        self.edge5.set_color(color=GREEN)
        self.wait(1)
        self.play(node_E.animate.shift(5 * LEFT), wnode6.animate.shift(4.8 * LEFT+0.2*UP))
        edge4 = Arrow(node_D, node_E, stroke_width=3, max_tip_length_to_length_ratio=0.1, buff=0.05)
        self.play(Create(edge4))
        self.edge7.set_color(color=GREEN)
        self.wait(1)
        self.play(node_T.animate.shift(4 * LEFT), wnode7.animate.shift(4.2 * LEFT))
        edge5 = Arrow(node_E, node_T, stroke_width=3, max_tip_length_to_length_ratio=0.1, buff=0.05)
        self.play(Create(edge5))
        self.edge8.set_color(color=GREEN)
        self.wait(1)
        self.play(node_C.animate.shift(3 * LEFT+1*UP), wnode4.animate.shift(3 * LEFT+ 0.8*UP))
        edge6 = Arrow(node_A, node_C, stroke_width=3, max_tip_length_to_length_ratio=0.1, buff=0.05)
        self.play(Create(edge6))
        self.edge3.set_color(color=GREEN)
        self.wait(1)
        mstGroup=Group(self.edge1.copy(),self.edge4.copy(),self.edge5.copy(),self.edge7.copy(),self.edge8.copy(),self.edge3.copy(),self.node_A.copy(),self.node_B.copy(),self.node_C.copy(),self.node_D.copy(),self.node_E.copy(),self.node_T.copy(),self.weight_label1.copy(),self.weight_label4.copy(),self.weight_label5.copy(),self.weight_label7.copy(),self.weight_label8.copy(),self.weight_label3.copy(),self.wnode1.copy(),self.wnode2.copy(),self.wnode3.copy(),self.wnode4.copy(),self.wnode6.copy(),self.wnode5.copy(),self.wnode7.copy())
        self.play(mstGroup.animate.shift(3*DOWN))
        self.edge3.set_color(color=WHITE)
        self.edge8.set_color(color=WHITE)
        self.edge7.set_color(color=WHITE)
        self.edge5.set_color(color=WHITE)
        self.edge4.set_color(color=WHITE)
        self.edge1.set_color(color=WHITE)
        self.play(self.group.animate.shift(1* UP))



        self.wait(3)

    def makeGraph(self):
        self.node_S = Dot(point=np.array([-3, 1, 0]))
        self.node_A = Dot(point=np.array([0, 2, 0]))
        self.node_C = Dot(point=np.array([3, 3, 0]))
        self.node_D = Dot(point=np.array([2, 1, 0]))
        self.node_B = Dot(point=np.array([0, -1, 0]))
        self.node_E = Dot(point=np.array([3, -1, 0]))
        self.node_T = Dot(point=np.array([4, 1, 0]))

        # Create edge with a label (weight)
        self.edge1 = Arrow(self.node_S, self.node_A, buff=0.05)
        self.edge2 = Arrow(self.node_S, self.node_B, buff=0.05)
        self.edge3 = Arrow(self.node_A, self.node_C, buff=0.05)
        self.edge4 = Arrow(self.node_A, self.node_D, buff=0.05)
        self.edge5 = Arrow(self.node_B, self.node_D, buff=0.05)
        self.edge6 = Arrow(self.node_D, self.node_T, buff=0.05)
        self.edge7 = Arrow(self.node_D, self.node_E, buff=0.05)
        self.edge8 = Arrow(self.node_E, self.node_T, buff=0.05)
        self.edge9 = Arrow(self.node_B, self.node_E, buff=0.05)
        self.edge10 = Arrow(self.node_C, self.node_T, buff=0.05)

        self.weight_label1 = Tex("10", color=WHITE, font_size=30).shift(1.65 * UP + 2 * LEFT)
        self.weight_label2 = Tex("20", color=WHITE, font_size=30).shift(2 * LEFT)
        self.weight_label3 = Tex("20", color=WHITE, font_size=30).shift(2.65 * UP + 1 * RIGHT)
        self.weight_label4 = Tex("10", color=WHITE, font_size=30).shift(1.2 * UP, 0.8 * RIGHT)
        self.weight_label5 = Tex("10", color=WHITE, font_size=30).shift(0.6 * RIGHT)
        self.weight_label6 = Tex("40", color=WHITE, font_size=30).shift(1.3 * UP + 2.7 * RIGHT)
        self.weight_label7 = Tex("10", color=WHITE, font_size=30).shift(2.9 * RIGHT)
        self.weight_label8 = Tex("10", color=WHITE, font_size=30).shift(3.9 * RIGHT)
        self.weight_label9 = Tex("10", color=WHITE, font_size=30).shift(0.8 * DOWN + 1.5 * RIGHT)
        self.weight_label10 = Tex("30", color=WHITE, font_size=30).shift(2.5 * UP + 3.7 * RIGHT)

        self.wnode1 = Tex("S", color=WHITE, font_size=30).next_to(self.node_S, LEFT)
        self.wnode2 = Tex("A", color=WHITE, font_size=30).next_to(self.node_A, UP)
        self.wnode3 = Tex("B", color=WHITE, font_size=30).next_to(self.node_B, DOWN)
        self.wnode4 = Tex("C", color=WHITE, font_size=30).next_to(self.node_C, UP)
        self.wnode5 = Tex("D", color=WHITE, font_size=30).next_to(self.node_D, UP)
        self.wnode6 = Tex("E", color=WHITE, font_size=30).next_to(self.node_E, DOWN)
        self.wnode7 = Tex("T", color=WHITE, font_size=30).next_to(self.node_T, RIGHT)
        self.group=VGroup(self.node_S,self.node_A,self.node_B,self.node_C,self.node_D,self.node_E,self.node_T,self.edge1,self.edge2,self.edge3,self.edge4,self.edge5,self.edge6,self.edge7,self.edge8,self.edge9,self.edge10,self.wnode1,self.wnode2,self.wnode3,self.wnode4,self.wnode5,self.wnode6,self.wnode7,self.weight_label1,self.weight_label2,self.weight_label3,self.weight_label3,self.weight_label4,self.weight_label5,self.weight_label6,self.weight_label7,self.weight_label8,self.weight_label9,self.weight_label10)

        # self.play(Create(edge), Write(weight_label))
        # Display nodes and edge
        nodeGroup=Group(self.node_S,self.node_A,self.node_B,self.node_C,self.node_D,self.node_E,self.node_T)
        self.play(FadeIn(nodeGroup))
        self.play(Create(self.edge1), Create(self.edge2), Create(self.edge3), Create(self.edge4), Create(self.edge5), Create(self.edge6),
                  Create(self.edge7), Create(self.edge8), Create(self.edge9), Create(self.edge10), Write(self.weight_label1),
                  Write(self.weight_label2), Write(self.weight_label3), Write(self.weight_label4), Write(self.weight_label5),
                  Write(self.weight_label6), Write(self.weight_label7), Write(self.weight_label8), Write(self.weight_label9),
                  Write(self.weight_label10), Write(self.wnode1), Write(self.wnode2), Write(self.wnode3), Write(self.wnode4), Write(self.wnode5),
                  Write(self.wnode6), Write(self.wnode7))


