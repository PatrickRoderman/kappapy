""" Returns the calculated Cohen's Kappa; inter-rater agreement statistic,
    given binary oveservations from two raters """
def kappa(rater1, rater2):
    """ Returns the calculated Cohen's Kappa; inter-rater agreement statistic.
        @params rater1: array containing binary observations of length n
        @params rater2: array containing binary observations of length n
        returns double """
    def calc_matrix(rater1, rater2):
        """returns agreement matrix from two binary observation arrays"""
        # 2x2 agreement matrix
        agreement_matrix = [[0 for i in range(2)] for i in range(2)]
        if len(rater1) == len(rater2):
            for i in range(len(rater1)):
                observation1 = rater1[i]
                observation2 = rater2[i]
                if observation1 == observation2:
                    if observation1 == 1:
                        agreement_matrix[1][1] = agreement_matrix[1][1] + 1
                    elif observation1 == 0:
                        agreement_matrix[0][0] = agreement_matrix[0][0] + 1
                    else:
                        raise Exception('Observations are not binary. [Array index ' + i + ']')
                else:
                    if observation1 == 1 and observation2 == 0:
                        agreement_matrix[1][0] = agreement_matrix[1][0] + 1
                    elif observation1 == 0 and observation2 == 1:
                        agreement_matrix[0][1] = agreement_matrix[0][1] + 1
                    else:
                        raise Exception('Observations are not binary. [Array index ' + i + ']')
            return agreement_matrix
        else:
            raise Exception('Observations parameters have different array lengths.')
    def calc_kappa(agreement_matrix):
        """Return Kappa value using agreement matrix"""
        try:
            p_o = ((agreement_matrix[0][0] + agreement_matrix[1][1]) /
                   (agreement_matrix[0][0] + agreement_matrix[0][1] +
                    agreement_matrix[1][0] + agreement_matrix[1][1]))
            p_yes = ((agreement_matrix[0][0] + agreement_matrix[1][0]) /
                     (agreement_matrix[0][0] + agreement_matrix[0][1] +
                      agreement_matrix[1][0] + agreement_matrix[1][1]) *
                     ((agreement_matrix[0][0] + agreement_matrix[0][1]) /
                      (agreement_matrix[0][0] + agreement_matrix[0][1] +
                       agreement_matrix[1][0] + agreement_matrix[1][1])))
            p_no = ((agreement_matrix[0][1] + agreement_matrix[1][1]) /
                    (agreement_matrix[0][0] + agreement_matrix[0][1] +
                     agreement_matrix[1][0] + agreement_matrix[1][1])*
                    ((agreement_matrix[1][1] + agreement_matrix[1][0]) /
                     (agreement_matrix[0][0] + agreement_matrix[0][1] +
                      agreement_matrix[1][0] + agreement_matrix[1][1])))
            p_e = p_yes + p_no
            return (p_o - p_e) / (1 - p_e)
        except ZeroDivisionError:
            raise Exception("Agreement matrix too sparse.")
    # populate agreement matrix given arrays of binary observations from two raters
    agreement_matrix = calc_matrix(rater1, rater2)
    # return the kappa based on complete matrix
    return calc_kappa(agreement_matrix)
