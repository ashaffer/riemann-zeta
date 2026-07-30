import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk10 :
    P2RoundedFactorCheckpointData.panel9Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix40_eq :
    P2RoundedFactorCheckpointData.panel9Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk10.1

theorem panel9Prefix41_eq :
    P2RoundedFactorCheckpointData.panel9Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk10.2.1

theorem panel9Prefix42_eq :
    P2RoundedFactorCheckpointData.panel9Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk10.2.2.1

theorem panel9Prefix43_eq :
    P2RoundedFactorCheckpointData.panel9Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk10.2.2.2

end RHP2Bridge
