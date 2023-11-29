import numpy as np
from manim import *
from manim_pptx import PPTXScene
#from manim_slides import Slide

import os
os.environ['FFMPEG_BIN'] = 'C:\\Users\\modic\\anaconda3\\envs\\my-manim\\Lib\\site-packages\\ffmpeg'
config.max_files_cached=250
class DirectedWeightedGraph(PPTXScene):
    def construct(self):
        self.begin()
        self.makeInitialGraph()
        self.startPrims()
        self.psuedoAlgo()
        self.makeGraph()
        self.makeGraph2()

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
        self.endSlide()
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text5),FadeOut(text6),FadeOut(text7),FadeOut(text8),FadeOut(text9),FadeOut(text10))



    def begin(self):
        text1 = Tex(r"PRIM'S ALGORITHM ", color=BLUE, font_size=40)
        self.play(Write(text1))
        self.play(text1.animate.shift(3 * UP + 5 * LEFT))
        self.endSlide()
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
        self.endSlide()
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
        self.endSlide()
        self.play(node_A.animate.shift(4*LEFT),wnode2.animate.shift(4*LEFT+0.2*DOWN))
        edge1 = Line(node_S, node_A,stroke_width=3, buff=0.05)
        self.play(Create(edge1))
        self.edge1.set_color(color=GREEN)

        self.wait(1)
        self.endSlide()
        self.play(node_D.animate.shift(5 * LEFT+2*DOWN), wnode5.animate.shift(4.75 * LEFT+2.3*DOWN))
        edge2 = Line(node_A, node_D, stroke_width=3, buff=0.05)
        self.play(Create(edge2))
        self.edge4.set_color(color=GREEN)

        self.wait(1)
        self.endSlide()
        self.play(node_B.animate.shift(6 * LEFT + 2 * DOWN), wnode3.animate.shift(6 * LEFT + 1.8 * DOWN))
        edge3 = Line(node_D, node_B, stroke_width=3, buff=0.05)
        self.play(Create(edge3))
        self.edge5.set_color(color=GREEN)

        self.wait(1)
        self.endSlide()
        self.play(node_E.animate.shift(5 * LEFT), wnode6.animate.shift(4.8 * LEFT+0.2*UP))
        edge4 = Line(node_D, node_E, stroke_width=3, buff=0.05)
        self.play(Create(edge4))
        self.edge7.set_color(color=GREEN)

        self.wait(1)
        self.endSlide()
        self.play(node_T.animate.shift(4 * LEFT), wnode7.animate.shift(4.2 * LEFT))
        edge5 = Line(node_E, node_T, stroke_width=3, buff=0.05)
        self.play(Create(edge5))
        self.edge8.set_color(color=GREEN)

        self.wait(1)
        self.endSlide()
        self.play(node_C.animate.shift(3 * LEFT+1*UP), wnode4.animate.shift(3 * LEFT+ 0.8*UP))
        edge6 = Line(node_A, node_C, stroke_width=3, buff=0.05)
        self.play(Create(edge6))
        self.edge3.set_color(color=GREEN)

        self.wait(1)
        self.endSlide()
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
        self.endSlide()
        self.play(FadeOut(mstGroup),FadeOut(self.group),FadeOut(edgeGroup),FadeOut(node_group),FadeOut(ellipse_group),FadeOut(textGroup))

    def makeInitialGraph(self):
        self.node_S = Dot(point=np.array([-3, 1, 0]))
        self.node_A = Dot(point=np.array([0, 2, 0]))
        self.node_C = Dot(point=np.array([3, 3, 0]))
        self.node_D = Dot(point=np.array([2, 1, 0]))
        self.node_B = Dot(point=np.array([0, -1, 0]))
        self.node_E = Dot(point=np.array([3, -1, 0]))
        self.node_T = Dot(point=np.array([4, 1, 0]))

        # Create edge with a label (weight)
        self.edge1 = Line(self.node_S, self.node_A, buff=0.05)
        self.edge2 = Line(self.node_S, self.node_B, buff=0.05)
        self.edge3 = Line(self.node_A, self.node_C, buff=0.05)
        self.edge4 = Line(self.node_A, self.node_D, buff=0.05)
        self.edge5 = Line(self.node_B, self.node_D, buff=0.05)
        self.edge6 = Line(self.node_D, self.node_T, buff=0.05)
        self.edge7 = Line(self.node_D, self.node_E, buff=0.05)
        self.edge8 = Line(self.node_E, self.node_T, buff=0.05)
        self.edge9 = Line(self.node_B, self.node_E, buff=0.05)
        self.edge10 = Line(self.node_C, self.node_T, buff=0.05)

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
        self.endSlide()

    def makeGraph(self):
        self.text0 = Tex(r"Assumption: Given a Graph with unique weight edges", font_size=35, color=WHITE)

        self.text99 = Tex(r"Let prove Prim's Algorithm by induction on number of iterations the algorithm runs",
                          font_size=35, color=WHITE)
        self.play(
            FadeIn(self.text0)
        )
        self.endSlide()
        self.wait(3)
        self.remove(self.text0)
        self.play(
            FadeIn(self.text99)
        )
        self.endSlide()
        self.wait(3)
        self.remove(self.text99)
        self.node_D = Dot(point=np.array([3, -1, 0]))
        self.node_A = Dot(point=np.array([0, -2, 0]))
        self.node_C = Dot(point=np.array([-2, -3, 0]))
        self.node_S = Dot(point=np.array([-2, -1, 0]))
        self.node_B = Dot(point=np.array([0, 1, 0]))
        self.node_E = Dot(point=np.array([-3, 1, 0]))
        self.node_T = Dot(point=np.array([-4, -1, 0]))

        # Create edge with a label (weight)
        self.edge1 = Line(self.node_D, self.node_A)
        self.edge2 = Line(self.node_D, self.node_B)
        self.edge3 = Line(self.node_A, self.node_C)
        self.edge4 = Line(self.node_A, self.node_S)
        self.edge5 = Line(self.node_B, self.node_S)
        self.edge6 = Line(self.node_S, self.node_T)
        self.edge7 = Line(self.node_S, self.node_E)
        self.edge8 = Line(self.node_E, self.node_T)
        self.edge9 = Line(self.node_A, self.node_B)

        self.w1 = Tex("D", color=WHITE, font_size=40).next_to(self.node_D)
        self.w2 = Tex("A", color=WHITE, font_size=40).next_to(self.node_A, DOWN)
        self.w3 = Tex("B", color=WHITE, font_size=40).next_to(self.node_B)
        self.w4 = Tex("C", color=WHITE, font_size=40).next_to(self.node_C, DOWN)
        self.w5 = Tex("S", color=WHITE, font_size=40).next_to(self.node_S)
        self.w6 = Tex("E", color=WHITE, font_size=40).next_to(self.node_E)
        self.w7 = Tex("T", color=WHITE, font_size=40).next_to(self.node_T, DOWN)

        # self.play(Create(edge), Write(weight_label))
        # Display nodes and edge
        nodeGroup = Group(self.node_D, self.node_A, self.node_B, self.node_C, self.node_S, self.node_E, self.node_T)
        self.play(FadeIn(nodeGroup))
        self.play(Create(self.edge1), Create(self.edge2), Create(self.edge3), Create(self.edge4), Create(self.edge5),
                  Create(self.edge6),
                  Create(self.edge7), Create(self.edge8), Create(self.edge9), Write(self.w1), Write(self.w2),
                  Write(self.w3), Write(self.w4), Write(self.w5),
                  Write(self.w6), Write(self.w7))
        #self.endSlide()
        self.node_S.set_color(RED)
        self.endSlide()
        self.Lemma = Tex(r"Lemma: The First edge added by our algorithm lies in MST", font_size=40,
                         color=WHITE).to_edge(UP)
        self.add(self.Lemma)
        self.play(
            FadeIn(self.Lemma)

        )

        self.wait(1)
        self.endSlide()
        self.play(
            self.w1.animate.next_to(np.array([3, -1.5, 0])),
            self.w2.animate.next_to(np.array([0, -1, 0]), DOWN),
            self.w3.animate.next_to(np.array([1, 0, 0])),
            self.w4.animate.next_to(np.array([2, -3, 0])),
            self.w6.animate.next_to(np.array([1, 1, 0])),
            self.w7.animate.next_to(np.array([2, 2, 0])),
            self.w5.animate.next_to(np.array([-3, 0, 0]), LEFT),

            self.node_D.animate.move_to(np.array([3, -1.5, 0])),
            self.node_A.animate.move_to(np.array([0, -1, 0])),
            self.node_B.animate.move_to(np.array([1, 0, 0])),
            self.node_C.animate.move_to(np.array([2, -3, 0])),
            self.node_E.animate.move_to(np.array([1, 1, 0])),
            self.node_T.animate.move_to(np.array([2, 2, 0])),
            self.node_S.animate.move_to(np.array([-3, 0, 0])),

            self.edge1.animate.put_start_and_end_on(np.array([3, -1.5, 0]), np.array([0, -1, 0])),
            self.edge2.animate.put_start_and_end_on(np.array([3, -1.5, 0]), np.array([1, 0, 0])),
            self.edge3.animate.put_start_and_end_on(np.array([0, -1, 0]), np.array([2, -3, 0])),
            self.edge8.animate.put_start_and_end_on(np.array([1, 1, 0]), np.array([2, 2, 0])),
            self.edge9.animate.put_start_and_end_on(np.array([0, -1, 0]), np.array([1, 0, 0])),
            self.edge4.animate.put_start_and_end_on(np.array([0, -1, 0]), np.array([-3, 0, 0])),
            self.edge5.animate.put_start_and_end_on(np.array([1, 0, 0]), np.array([-3, 0, 0])),
            self.edge6.animate.put_start_and_end_on(np.array([-3, 0, 0]), np.array([2, 2, 0])),
            self.edge7.animate.put_start_and_end_on(np.array([-3, 0, 0]), np.array([1, 1, 0]))

        )


        self.remove(self.Lemma)
        self.endSlide()
        self.text1 = Tex(r"Node S divides the graph in two subgraph having different MST connected through S",
                         font_size=40, color=WHITE).to_edge(UP)
        subgraph1 = Group(self.node_D, self.node_A, self.node_B, self.node_C, self.w1, self.w2, self.w3, self.w4,
                          self.edge1, self.edge2, self.edge3, self.edge9)
        subgraph2 = Group(self.node_E, self.node_T, self.w6, self.w7, self.edge8)
        self.play(FadeIn(self.text1))
        self.play(Wiggle(subgraph1))
        self.play(Wiggle(subgraph2))
        self.remove(self.text1)

        ellipse_right = Ellipse(width=2.5, height=6, color=BLUE)
        ellipse_left = Ellipse(width=2.5, height=6, color=BLUE)
        right_group = Group(self.node_D, self.node_A, self.node_B, self.node_C, self.node_E, self.node_T, self.w1,
                            self.w2, self.w3, self.w4, self.w6, self.w7, self.edge1, self.edge2, self.edge3, self.edge8,
                            self.edge9, self.node_S, self.w5, self.edge4, self.edge5, self.edge6, self.edge7)
        self.play(
            right_group.animate.scale(0.7)

        )
        ellipse_right.move_to(self.node_S.get_center()),
        ellipse_left.move_to(self.node_B.get_center() + 0.5 * RIGHT)
        self.play(
            Create(ellipse_right),
            Create(ellipse_left)
        )

        self.wait(1)
        self.endSlide()
        self.text2 = Tex(
            r"Let assume contradictory that minimum edge wieght namely SB chosen by our algorithm is not part of MST",
            font_size=35, color=WHITE).to_edge(UP)
        self.add(self.text2)
        self.MST_edge = DashedLine(self.node_S, self.node_B, dash_length=0.3)
        self.MST_edge.set_color(GREEN)
        self.MST_edge.set_stroke(width=8)
        edgename = Tex(r"Minimum weight edge", font_size=35, color=WHITE)
        edgename.next_to(self.MST_edge, UP, buff=0.1)
        self.play(
            FadeIn(self.text2),
            Create(self.MST_edge),
            Write(edgename, run_time=1)
        )
        self.wait(2)
        self.endSlide()
        self.remove(self.text2)
        self.remove(edgename)
        both_ellipses = Group(ellipse_left, ellipse_right, right_group, self.MST_edge)
        self.play(both_ellipses.animate.shift(RIGHT * 3))
        self.play(both_ellipses.animate.scale(0.9))
        self.text3 = Tex(r"Let the MST is given by RED Line", font_size=40, color=WHITE).to_edge(UP)
        self.edge10 = Line(self.node_S, self.node_A)
        self.edge11 = Line(self.node_S, self.node_E)

        self.edge1.set_color(RED),
        self.edge1.set_stroke(width=8),
        self.edge2.set_color(RED),
        self.edge2.set_stroke(width=8),
        self.edge3.set_color(RED),
        self.edge3.set_stroke(width=8),
        self.edge8.set_color(RED),
        self.edge8.set_stroke(width=8),
        self.edge10.set_color(RED),
        self.edge10.set_stroke(width=8),
        self.edge11.set_color(RED),
        self.edge11.set_stroke(width=8),
        self.play(
            FadeIn(self.text3),
            Create(self.edge11),
            Create(self.edge10)
        )
        self.endSlide()
        MSTwithout_min_wieght_edge = Group(self.w1, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7, self.node_A,
                                           self.node_B, self.node_C, self.node_D, self.node_S, self.node_E, self.node_T,
                                           self.edge1, self.edge2, self.edge3, self.edge8, self.edge10, self.edge11)
        copy_MSTwithout_min_wieght = MSTwithout_min_wieght_edge.copy()
        NameofTree = Tex(r"T", font_size=30, color=GOLD)
        self.play(copy_MSTwithout_min_wieght.animate.shift(7.5 * LEFT + 2 * UP))
        self.play(copy_MSTwithout_min_wieght.animate.scale(0.8))
        NameofTree.next_to(copy_MSTwithout_min_wieght, DOWN, buff=0.1)
        self.play(Write(NameofTree))
        self.endSlide()
        self.wait(2)
        self.remove(self.text3)
        self.text4 = Tex(r"Now connecting the minimum edge weight SB to graph forms a cycle of GREEN color",
                         font_size=40, color=WHITE).to_edge(UP)
        self.play(
            FadeIn(self.text4),

        )
        self.edge1.set_color(GREEN)
        self.edge1.set_stroke(width=8)
        self.edge2.set_color(GREEN)
        self.edge2.set_stroke(width=8)
        self.edge10.set_color(GREEN)
        self.edge10.set_stroke(width=8)
        self.wait(2)
        self.endSlide()
        self.remove(self.text4)
        self.wait(2)
        self.text5 = Tex("Now Removing the edge SA aand adding edge SB gives another MST say T-SA+SB", font_size=35,
                         color=WHITE).to_edge(UP)
        self.play(FadeIn(self.text5))
        self.remove(self.MST_edge)
        self.new_MST_edge = Line(self.node_S, self.node_B)
        self.new_MST_edge.set_color(GREEN)
        self.new_MST_edge.set_stroke(width=8)
        self.play(
            FadeOut(self.edge10),
            FadeIn(self.new_MST_edge),
        )
        self.endSlide()
        self.wait(3)
        self.new_MST_edge.set_color(RED)
        self.edge1.set_color(RED)
        self.edge2.set_color(RED)
        self.wait(1)

        self.edge1.set_stroke(width=8)
        self.edge2.set_stroke(width=8)
        self.new_MST_edge.set_stroke(width=8)
        self.endSlide()
        MSTwith_min_weight_edge = Group(self.w1, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7, self.node_A,
                                        self.node_B, self.node_C, self.node_D, self.node_S, self.node_E, self.node_T,
                                        self.edge1, self.edge2, self.edge3, self.edge8, self.new_MST_edge, self.edge11)
        copyMSTwith_min_weight_edge = MSTwith_min_weight_edge.copy()
        self.play(copyMSTwith_min_weight_edge.animate.shift(7.5 * LEFT + 1 * DOWN))
        self.play(copyMSTwith_min_weight_edge.animate.scale(0.8))
        NameofTree2 = Tex(r"T-SA+SB", font_size=30, color=GOLD)
        NameofTree2.next_to(copyMSTwith_min_weight_edge, DOWN, buff=0.1)
        self.play(Write(NameofTree2))
        self.endSlide()
        self.remove(self.text5)
        right_part = Group(MSTwith_min_weight_edge, ellipse_left, ellipse_right, self.edge9)
        self.play(FadeOut(right_part),
                  FadeOut(self.edge6),
                  FadeOut(self.edge7),
                  FadeOut(self.edge4),
                  FadeOut(self.edge5))
        right_MST = Group(copyMSTwith_min_weight_edge, NameofTree2)
        self.play(right_MST.animate.shift(6 * RIGHT + 3 * UP))
        text7 = Tex(r"The $weight(T) > weight(T+SA-SB)$ which is a contradiction because we assume that T is a MST",
                    font_size=40, color=WHITE).to_edge(DOWN)
        self.play(FadeIn(text7))
        self.wait(3)
        left_MST = Group(copy_MSTwithout_min_wieght, NameofTree)
        self.play(
            FadeOut(text7),
            FadeOut(right_MST),
            FadeOut(left_MST)
        )
        self.endSlide()

    def makeGraph2(self):
        self.Lemma = Tex(r"By induction hypothesis there would be an MST by prims on left set", font_size=40,
                         color=WHITE).to_edge(UP)
        self.add(self.Lemma)
        self.play(
            FadeIn(self.Lemma)

        )
        self.wait(2)
        self.endSlide()
        self.node_D = Dot(point=np.array([3, -1, 0]))
        self.node_A = Dot(point=np.array([0, -2, 0]))
        self.node_C = Dot(point=np.array([-2, -3, 0]))
        self.node_S = Dot(point=np.array([-2, -1, 0]))
        self.node_B = Dot(point=np.array([0, 1, 0]))
        self.node_E = Dot(point=np.array([-3, 1, 0]))
        self.node_T = Dot(point=np.array([-4, -1, 0]))

        # Create edge with a label (weight)
        self.edge1 = Line(self.node_D, self.node_A)
        self.edge2 = Line(self.node_D, self.node_B)
        self.edge3 = Line(self.node_A, self.node_C)
        self.edge4 = Line(self.node_A, self.node_S)
        self.edge5 = Line(self.node_B, self.node_S)
        self.edge6 = Line(self.node_S, self.node_T)
        self.edge7 = Line(self.node_S, self.node_E)
        self.edge8 = Line(self.node_E, self.node_T)
        self.edge9 = Line(self.node_A, self.node_B)

        self.w1 = Tex("D", color=WHITE, font_size=40).next_to(self.node_D)
        self.w2 = Tex("A", color=WHITE, font_size=40).next_to(self.node_A, DOWN)
        self.w3 = Tex("B", color=WHITE, font_size=40).next_to(self.node_B)
        self.w4 = Tex("C", color=WHITE, font_size=40).next_to(self.node_C, DOWN)
        self.w5 = Tex("S", color=WHITE, font_size=40).next_to(self.node_S)
        self.w6 = Tex("E", color=WHITE, font_size=40).next_to(self.node_E)
        self.w7 = Tex("T", color=WHITE, font_size=40).next_to(self.node_T, DOWN)

        # self.play(Create(edge), Write(weight_label))
        # Display nodes and edge
        nodeGroup = Group(self.node_D, self.node_A, self.node_B, self.node_C, self.node_S, self.node_E, self.node_T)
        self.play(FadeIn(nodeGroup))
        self.play(Create(self.edge1), Create(self.edge2), Create(self.edge3), Create(self.edge4), Create(self.edge5),
                  Create(self.edge6),
                  Create(self.edge7), Create(self.edge8), Create(self.edge9), Write(self.w1), Write(self.w2),
                  Write(self.w3), Write(self.w4), Write(self.w5),
                  Write(self.w6), Write(self.w7))
        self.node_S.set_color(RED)
        self.node_B.set_color(RED)
        self.wait(1)
        self.play(
            self.w5.animate.next_to(np.array([-3, 0, 0]), LEFT),
            self.w3.animate.next_to(np.array([-2.5, -2, 0]), LEFT),
            self.w1.animate.next_to(np.array([1, -1.5, 0])),
            self.w2.animate.next_to(np.array([0, -1, 0]), DOWN),
            self.w4.animate.next_to(np.array([2, 0, 0])),
            self.w6.animate.next_to(np.array([1, 1, 0])),
            self.w7.animate.next_to(np.array([2, 2, 0])),

            self.node_D.animate.move_to(np.array([1, -1.5, 0])),
            self.node_A.animate.move_to(np.array([0, -1, 0])),
            self.node_C.animate.move_to(np.array([2, 0, 0])),
            self.node_E.animate.move_to(np.array([1, 1, 0])),
            self.node_T.animate.move_to(np.array([2, 2, 0])),
            self.node_S.animate.move_to(np.array([-3, 0, 0])),
            self.node_B.animate.move_to(np.array([-2.5, -2, 0])),

            self.edge1.animate.put_start_and_end_on(np.array([1, -1.5, 0]), np.array([0, -1, 0])),
            self.edge2.animate.put_start_and_end_on(np.array([1, -1.5, 0]), np.array([-2.5, -2, 0])),
            self.edge3.animate.put_start_and_end_on(np.array([0, -1, 0]), np.array([2, 0, 0])),
            self.edge8.animate.put_start_and_end_on(np.array([1, 1, 0]), np.array([2, 2, 0])),
            self.edge9.animate.put_start_and_end_on(np.array([0, -1, 0]), np.array([-2.5, -2, 0])),
            self.edge4.animate.put_start_and_end_on(np.array([0, -1, 0]), np.array([-3, 0, 0])),
            self.edge5.animate.put_start_and_end_on(np.array([-2.5, -2, 0]), np.array([-3, 0, 0])),
            self.edge6.animate.put_start_and_end_on(np.array([-3, 0, 0]), np.array([2, 2, 0])),
            self.edge7.animate.put_start_and_end_on(np.array([-3, 0, 0]), np.array([1, 1, 0]))

        )
        self.endSlide()
        self.remove(self.Lemma)
        self.mst_statement = Tex(
            r"we would have edges on left set which would be part of MST denoted by Red color by induction hypothesis",
            font_size=40, color=WHITE).to_edge(UP)
        self.edge5.set_color(RED)
        self.edge5.set_stroke(width=10)
        self.wait(3)
        self.endSlide()
        self.mst_statement.remove()
        ellipse_right = Ellipse(width=2.5, height=6, color=BLUE)
        ellipse_left = Ellipse(width=2.5, height=6, color=BLUE)
        right_group = Group(self.node_D, self.node_A, self.node_B, self.node_C, self.node_E, self.node_T, self.w1,
                            self.w2, self.w3, self.w4, self.w6, self.w7, self.edge1, self.edge2, self.edge3, self.edge8,
                            self.edge9, self.node_S, self.w5, self.edge4, self.edge5, self.edge6, self.edge7)
        self.play(
            right_group.animate.scale(0.8)
        )
        ellipse_right.move_to(self.node_S.get_center())
        ellipse_left.move_to(self.node_C.get_center() + 1 * LEFT)
        self.play(
            Create(ellipse_right),
            Create(ellipse_left)
        )

        self.wait(1)
        self.endSlide()
        self.text2 = Tex(r"Let assume contradictory that minimum edge wieght  is BA and is not a part of MST",
                         font_size=35, color=WHITE).to_edge(UP)
        self.add(self.text2)
        self.MST_edge = DashedLine(self.node_B, self.node_A, dash_length=0.3)
        self.MST_edge.set_color(GREEN)
        self.MST_edge.set_stroke(width=8)
        edgename = Tex(r"Minimum weight edge", font_size=35, color=WHITE)
        edgename.next_to(self.MST_edge, UP, buff=0.1)
        self.play(
            FadeIn(self.text2),
            Create(self.MST_edge),
            Write(edgename, run_time=1)
        )
        self.wait(2)
        self.endSlide()
        self.remove(self.text2)
        self.remove(edgename)
        both_ellipses = Group(ellipse_left, ellipse_right, right_group, self.MST_edge)
        self.play(both_ellipses.animate.shift(RIGHT * 3))
        self.play(both_ellipses.animate.scale(0.9))
        self.text3 = Tex(r"Let the MST is given by RED Line", font_size=40, color=WHITE).to_edge(UP)

        self.play(FadeIn(self.text3))
        self.edge5.set_color(RED)
        self.edge5.set_stroke(width=8)

        self.edge8.set_color(RED)
        self.edge8.set_stroke(width=8)
        self.edge7.set_color(RED)
        self.edge7.set_stroke(width=8)
        self.edge1.set_color(RED)
        self.edge1.set_stroke(width=8)
        self.edge2.set_color(RED)
        self.edge2.set_stroke(width=8)
        self.edge3.set_color(RED)
        self.edge3.set_stroke(width=8)
        self.edge8.set_color(RED)
        self.edge8.set_stroke(width=8)
        MSTwithout_min_wieght_edge = Group(self.w1, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7, self.node_A,
                                           self.node_B, self.node_C, self.node_D, self.node_S, self.node_E, self.node_T,
                                           self.edge1, self.edge2, self.edge3, self.edge8, self.edge5, self.edge7)
        copy_MSTwithout_min_wieght = MSTwithout_min_wieght_edge.copy()
        self.endSlide()
        NameofTree = Tex(r"T", font_size=30, color=GOLD)
        self.play(copy_MSTwithout_min_wieght.animate.shift(7.5 * LEFT + 2 * UP))
        self.play(copy_MSTwithout_min_wieght.animate.scale(0.9))
        NameofTree.next_to(copy_MSTwithout_min_wieght, DOWN, buff=0.1)
        self.play(Write(NameofTree))
        self.wait(2)
        self.remove(self.text3)
        self.text4 = Tex(r"Now connecting the minimum edge weight BA to graph forms a cycle of GREEN color",
                         font_size=40, color=WHITE).to_edge(UP)
        self.play(
            FadeIn(self.text4),

        )

        self.edge1.set_color(GREEN)
        self.edge1.set_stroke(width=8)
        self.edge2.set_color(GREEN)
        self.edge2.set_stroke(width=8)

        self.wait(2)
        self.endSlide()
        self.remove(self.text4)
        self.wait(2)
        self.text5 = Tex("Now Removing the edge BD aand adding edge BA gives another MST say T-BD+BA", font_size=35,
                         color=WHITE).to_edge(UP)
        self.play(FadeIn(self.text5))
        self.remove(self.MST_edge)
        self.edge9.set_color(RED)
        self.edge9.set_stroke(width=8)
        self.edge1.set_color(RED)
        self.edge2.set_stroke(width=4)
        self.edge2.set_color(WHITE)
        self.wait(2)
        MSTwith_min_weight_edge = Group(self.w1, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7, self.node_A,
                                        self.node_B, self.node_C, self.node_D, self.node_S, self.node_E, self.node_T,
                                        self.edge1, self.edge9, self.edge3, self.edge8, self.edge5, self.edge7)
        copyMSTwith_min_weight_edge = MSTwith_min_weight_edge.copy()
        self.play(copyMSTwith_min_weight_edge.animate.shift(7.5 * LEFT + 1 * DOWN))
        self.play(copyMSTwith_min_weight_edge.animate.scale(0.9))
        NameofTree2 = Tex(r"T-BD+BA", font_size=30, color=GOLD)
        NameofTree2.next_to(copyMSTwith_min_weight_edge, DOWN, buff=0.1)
        self.play(Write(NameofTree2))
        self.endSlide()
        self.remove(self.text5)
        right_part = Group(MSTwith_min_weight_edge, ellipse_left, ellipse_right, self.edge9)
        self.play(FadeOut(right_part),
                  FadeOut(self.edge6),
                  FadeOut(self.edge7),
                  FadeOut(self.edge4),
                  FadeOut(self.edge5),
                  FadeOut(self.edge2))
        right_MST = Group(copyMSTwith_min_weight_edge, NameofTree2)
        self.play(right_MST.animate.shift(6 * RIGHT + 3 * UP))
        text7 = Tex(r"The $weight(T) > weight(T+BD-BA)$ which is a contradiction because we assume that T is a MST",
                    font_size=40, color=WHITE).to_edge(DOWN)
        self.play(FadeIn(text7))
        self.wait(3)
        left_MST = Group(copy_MSTwithout_min_wieght, NameofTree)
        self.play(
            FadeOut(text7),
            FadeOut(right_MST),
            FadeOut(left_MST)
        )
        self.wait(3)
        self.endSlide()

