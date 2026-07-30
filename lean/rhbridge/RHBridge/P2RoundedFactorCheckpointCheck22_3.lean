import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk3 :
    P2RoundedFactorCheckpointData.panel22Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix12_eq :
    P2RoundedFactorCheckpointData.panel22Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk3.1

theorem panel22Prefix13_eq :
    P2RoundedFactorCheckpointData.panel22Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk3.2.1

theorem panel22Prefix14_eq :
    P2RoundedFactorCheckpointData.panel22Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk3.2.2.1

theorem panel22Prefix15_eq :
    P2RoundedFactorCheckpointData.panel22Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk3.2.2.2

end RHP2Bridge
