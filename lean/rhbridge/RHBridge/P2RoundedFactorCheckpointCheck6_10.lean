import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk10 :
    P2RoundedFactorCheckpointData.panel6Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix40_eq :
    P2RoundedFactorCheckpointData.panel6Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk10.1

theorem panel6Prefix41_eq :
    P2RoundedFactorCheckpointData.panel6Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk10.2.1

theorem panel6Prefix42_eq :
    P2RoundedFactorCheckpointData.panel6Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk10.2.2.1

theorem panel6Prefix43_eq :
    P2RoundedFactorCheckpointData.panel6Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk10.2.2.2

end RHP2Bridge
