import numpy as np
from manim import *
from manim_pptx import PPTXScene
class DirectedWeightedGraph(PPTXScene):
    def construct(self):
        self.begin()
        self.makeGraph()
        self.startPrims()
        self.psuedoAlgo()

    def psuedoAlgo(self):
        text1 = Tex(r"PSEUDOCODE: ", color=BLUE, font_size=30).move_to(3 * UP + 5 * LEFT)
        text2 = Tex(r"H = \{ S \}", color=WHITE, font_size=30).move_to(2.3 * UP + 5.5 * LEFT)
        text3 = Tex(r"WHILE (ALL VERTICES ARE NOT ADDED IN H)", color=WHITE, font_size=30).move_to(
            1.8 * UP + 2.5 * LEFT)
        text4 = Tex(r"\{", color=WHITE, font_size=30).move_to(1.3 * UP + 6.1 * LEFT)
        text5 = Tex(r"(U,V) $\leftarrow$  $\min_{\scriptscriptstyle  (U,V): U \in H , V \in Y} \{ W(U,V) \} $",
                    color=WHITE, font_size=30).move_to(0.8 * UP + 2.5 * LEFT)
        text6 = Tex(r"REMOVE V FROM Y AND ADD IT TO H", color=WHITE, font_size=30).move_to(0.3 * UP + 1.9 * LEFT)
        text7 = Tex(r"ADD (U,V) TO TREE", color=WHITE, font_size=30).move_to(0.2 * DOWN + 3.4 * LEFT)
        text8 = Tex(r"\}", color=WHITE, font_size=30).move_to(0.7 * DOWN + 6.1 * LEFT)
        text9 = Tex(r"RUNNING TIME: ", color=BLUE, font_size=30).move_to(1.7 * DOWN + 5 * LEFT)
        text10 = Tex(r"O((m+n)logn)", color=WHITE, font_size=30).move_to(1.7 * DOWN + 2.5 * LEFT)
        self.play(Write(text1), Write(text2), Write(text3), Write(text4), Write(text5), Write(text9), Write(text10),
                  Write(text6), Write(text7), Write(text8))
        self.wait(3)


    def begin(self):
        text1 = Tex(r"PRIM'S ALGORITHM ", color=BLUE, font_size=40)
        self.play(Write(text1))
        self.play(text1.animate.shift(3 * UP + 5 * LEFT))
        text2 = Tex(r"PROBLEM STATEMENT: ", color=BLUE, font_size=30).move_to(2 * UP + 5.25 * LEFT)
        self.play(Write(text2))
        text3 = Tex(
            r"$\bullet$ GIVEN   AN   UNDIRECTED   AND   WEIGHTED   GRAPH   G,   FIND   A   CONNECTED   SUBGRAPH   OF   G   OF   MINIMUM   WEIGHT",
            color=WHITE, font_size=20).move_to(1 * UP + 3.5 * LEFT)
        text4 = Tex(
            r"$\bullet$ FIND     A     SUBGRAPH     H    WHICH     HAS   $\text{MIN}_{\scriptscriptstyle   H \subseteq G} \{ WT(H) \}$ ,    WHERE     WT(H)= $\Sigma_{e \in H} \{ WT(e) \}$",
            color=WHITE, font_size=20).move_to(3.5 * LEFT)
        self.play(FadeIn(text3), FadeIn(text4))
        self.wait(3)
        group=Group(text2,text3,text4,text1)
        self.play(FadeOut(group))
    def startPrims(self):
        self.group.scale(0.6)
        self.play(self.group.animate.shift(4.5*LEFT))
        #self.wait(3)
        ellipse1 = Ellipse(
            width=3.0, height=5.0 ,stroke_width=7
        ).move_to(LEFT+0.8*UP)
        ellipse1.set_color(color=WHITE)
        ellipse2 = ellipse1.copy().set_color(color=WHITE).move_to(3*RIGHT+0.8*UP)
        ellipse_group = Group( ellipse1, ellipse2).move_to(RIGHT * 3)
        self.play(FadeIn(ellipse_group))
        mainIdea = Tex(
            r"OUR IDEA: BE GREEDY, FIND THE MINIMUM WEIGHT EDGE FROM H $ \rightarrow $ Y, SAY (U,V) THEN PULL V INTO H.",
            color=WHITE, font_size=20, tex_to_color_map={"OUR IDEA:": BLUE}).shift(3.2 * UP + 2 * RIGHT)
        # self.wait(3)

        bottomText1 = Tex(
            r"H IS SUBGRAPH THAT WE ARE MAKING",
            color=WHITE, font_size=20).shift(2.7 * DOWN + 1* RIGHT)
        # self.wait(3)
        bottomText2 = Tex(
            r"Y",
            color=WHITE, font_size=20).shift(2.7 * DOWN + 5 * RIGHT)
        self.play(Write(bottomText1), Write(bottomText2), Write(mainIdea))
        textGroup=Group(mainIdea,bottomText1,bottomText2)
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
        edgeGroup=Group(edge1,edge2,edge3,edge4,edge5,edge6)
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
        self.play(FadeOut(mstGroup),FadeOut(self.group),FadeOut(edgeGroup),FadeOut(node_group),FadeOut(ellipse_group),FadeOut(textGroup))

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


class BeginSlide(Scene):

    def construct(self):
        self.test()

    def test(self):
        text1 = Tex(r"PRIM'S ALGORITHM ", color=BLUE, font_size=40)
        self.play(Write(text1))
        self.play(text1.animate.shift(3*UP+5*LEFT))
        text2 = Tex(r"PROBLEM STATEMENT: ", color=BLUE, font_size=30).move_to(2*UP+5.25*LEFT)
        self.play(Write(text2))
        text3 = Tex(r"$\bullet$ GIVEN   AN   UNDIRECTED   AND   WEIGHTED   GRAPH   G,   FIND   A   CONNECTED   SUBGRAPH   OF   G   OF   MINIMUM   WEIGHT", color=WHITE, font_size=20).move_to(1*UP+3.5*LEFT)
        text4 = Tex(r"$\bullet$ FIND     A     SUBGRAPH     H    WHICH     HAS   $\text{MIN}_{\scriptscriptstyle   H \subseteq G} \{ WT(H) \}$ ,    WHERE     WT(H)= $\Sigma_{e \in H} \{ WT(e) \}$", color=WHITE, font_size=20).move_to(3.5*LEFT)
        self.play(FadeIn(text3),FadeIn(text4))

        self.wait(3)
class PrimAlgorithm(Scene):

    def construct(self):
        self.test()

    def test(self):
        text1=Tex(r"PSEUDOCODE: ",color=BLUE, font_size=30).move_to(3*UP+5*LEFT)
        text2 = Tex(r"H = \{ S \}", color=WHITE, font_size=30).move_to(2.3*UP+5.5*LEFT)
        text3 = Tex(r"WHILE (ALL VERTICES ARE NOT ADDED IN H)", color=WHITE, font_size=30).move_to(1.8*UP+2.5*LEFT)
        text4 = Tex(r"\{", color=WHITE, font_size=30).move_to(1.3*UP+6.1*LEFT)
        text5 = Tex(r"(U,V) $\leftarrow$  $\min_{\scriptscriptstyle  (U,V): U \in H , V \in Y} \{ W(U,V) \} $", color=WHITE, font_size=30).move_to(0.8*UP+2.5*LEFT)
        text6 = Tex(r"REMOVE V FROM Y AND ADD IT TO H", color=WHITE, font_size=30).move_to(0.3*UP+1.9*LEFT)
        text7 = Tex(r"ADD (U,V) TO TREE", color=WHITE, font_size=30).move_to(0.2*DOWN+3.4*LEFT)
        text8 = Tex(r"\}", color=WHITE, font_size=30).move_to(0.7 * DOWN + 6.1 * LEFT)
        text9 = Tex(r"RUNNING TIME: ", color=BLUE, font_size=30).move_to(1.7* DOWN + 5 * LEFT)
        text10 = Tex(r"O((m+n)logn)", color=WHITE, font_size=30).move_to(1.7 * DOWN + 2.5* LEFT)
        self.play(Write(text1),Write(text2),Write(text3),Write(text4),Write(text5),Write(text9),Write(text10), Write(text6),Write(text7),Write(text8))
        #text_object=VGroup(text1,text2,text3,text4,text5).arrange(DOWN,buff=0.1)
        #self.play(FadeIn(text_object))
        self.wait(3)
        # text1= Tex(
        #     r"PSEUDOCODE \\\\ H = \{ S \}"
        #     # r"WHILE (ALL VERTICES ARE NOT ADDED IN H) \n"
        #     # r"{"
        #     # r"\left(U < V\right) \rightarrow \min_{(U,V): U \in H, V \in Y} W_{U,V} \n"
        #     # r"REMOVE V FROM Y AND ADD IT TO H \n"
        #     # r"ADD (U,V) TO TREE \n"
        #     # r"}"
        #     ,
        #     color=WHITE, font_size=20)
        # self.play(Write(mainIdea))
        # self.wait(3)


        # mainIdea = Tex(
        #     r"OUR IDEA: BE GREEDY, FIND THE MINIMUM WEIGHT EDGE FROM H $ \rightarrow $ Y, SAY (U,V) THEN PULL V INTO H.",
        #     color=WHITE, font_size=20,tex_to_color_map={"OUR IDEA:":BLUE}).shift(3.2 * UP + 2 * RIGHT)
        # # self.wait(3)
        #
        # bottomText1 = Tex(
        #     r"H IS SUBGRAPH THAT WE ARE MAKING",
        #     color=WHITE, font_size=20).shift(2.7 * DOWN + 0.5 * RIGHT)
        # # self.wait(3)
        # bottomText2 = Tex(
        #     r"Y",
        #     color=WHITE, font_size=20).shift(2.7 * DOWN + 5* RIGHT)
        # self.play(Write(bottomText1), Write(bottomText2),Write(mainIdea))
