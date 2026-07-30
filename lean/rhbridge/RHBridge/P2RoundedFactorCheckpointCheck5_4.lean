import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk4 :
    P2RoundedFactorCheckpointData.panel5Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix16_eq :
    P2RoundedFactorCheckpointData.panel5Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk4.1

theorem panel5Prefix17_eq :
    P2RoundedFactorCheckpointData.panel5Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk4.2.1

theorem panel5Prefix18_eq :
    P2RoundedFactorCheckpointData.panel5Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk4.2.2.1

theorem panel5Prefix19_eq :
    P2RoundedFactorCheckpointData.panel5Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk4.2.2.2

end RHP2Bridge
