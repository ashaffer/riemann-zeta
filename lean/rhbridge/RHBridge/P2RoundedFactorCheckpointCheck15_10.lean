import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk10 :
    P2RoundedFactorCheckpointData.panel15Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix40_eq :
    P2RoundedFactorCheckpointData.panel15Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk10.1

theorem panel15Prefix41_eq :
    P2RoundedFactorCheckpointData.panel15Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk10.2.1

theorem panel15Prefix42_eq :
    P2RoundedFactorCheckpointData.panel15Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk10.2.2.1

theorem panel15Prefix43_eq :
    P2RoundedFactorCheckpointData.panel15Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk10.2.2.2

end RHP2Bridge
