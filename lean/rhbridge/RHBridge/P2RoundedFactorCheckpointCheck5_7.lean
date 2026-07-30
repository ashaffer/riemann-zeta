import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk7 :
    P2RoundedFactorCheckpointData.panel5Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix28_eq :
    P2RoundedFactorCheckpointData.panel5Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk7.1

theorem panel5Prefix29_eq :
    P2RoundedFactorCheckpointData.panel5Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk7.2.1

theorem panel5Prefix30_eq :
    P2RoundedFactorCheckpointData.panel5Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk7.2.2.1

theorem panel5Prefix31_eq :
    P2RoundedFactorCheckpointData.panel5Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk7.2.2.2

end RHP2Bridge
