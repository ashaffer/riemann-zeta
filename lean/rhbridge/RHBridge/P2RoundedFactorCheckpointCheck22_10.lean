import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk10 :
    P2RoundedFactorCheckpointData.panel22Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix40_eq :
    P2RoundedFactorCheckpointData.panel22Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk10.1

theorem panel22Prefix41_eq :
    P2RoundedFactorCheckpointData.panel22Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk10.2.1

theorem panel22Prefix42_eq :
    P2RoundedFactorCheckpointData.panel22Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk10.2.2.1

theorem panel22Prefix43_eq :
    P2RoundedFactorCheckpointData.panel22Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk10.2.2.2

end RHP2Bridge
