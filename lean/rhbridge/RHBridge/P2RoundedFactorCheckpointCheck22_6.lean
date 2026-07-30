import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk6 :
    P2RoundedFactorCheckpointData.panel22Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix24_eq :
    P2RoundedFactorCheckpointData.panel22Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk6.1

theorem panel22Prefix25_eq :
    P2RoundedFactorCheckpointData.panel22Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk6.2.1

theorem panel22Prefix26_eq :
    P2RoundedFactorCheckpointData.panel22Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk6.2.2.1

theorem panel22Prefix27_eq :
    P2RoundedFactorCheckpointData.panel22Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk6.2.2.2

end RHP2Bridge
