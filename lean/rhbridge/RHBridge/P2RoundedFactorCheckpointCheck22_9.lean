import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk9 :
    P2RoundedFactorCheckpointData.panel22Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix36_eq :
    P2RoundedFactorCheckpointData.panel22Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk9.1

theorem panel22Prefix37_eq :
    P2RoundedFactorCheckpointData.panel22Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk9.2.1

theorem panel22Prefix38_eq :
    P2RoundedFactorCheckpointData.panel22Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk9.2.2.1

theorem panel22Prefix39_eq :
    P2RoundedFactorCheckpointData.panel22Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk9.2.2.2

end RHP2Bridge
