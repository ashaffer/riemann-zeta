import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk10 :
    P2RoundedFactorCheckpointData.panel5Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix40_eq :
    P2RoundedFactorCheckpointData.panel5Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk10.1

theorem panel5Prefix41_eq :
    P2RoundedFactorCheckpointData.panel5Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk10.2.1

theorem panel5Prefix42_eq :
    P2RoundedFactorCheckpointData.panel5Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk10.2.2.1

theorem panel5Prefix43_eq :
    P2RoundedFactorCheckpointData.panel5Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk10.2.2.2

end RHP2Bridge
