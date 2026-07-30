import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk12 :
    P2RoundedFactorCheckpointData.panel22Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix48_eq :
    P2RoundedFactorCheckpointData.panel22Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk12.1

theorem panel22Prefix49_eq :
    P2RoundedFactorCheckpointData.panel22Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk12.2.1

theorem panel22Prefix50_eq :
    P2RoundedFactorCheckpointData.panel22Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk12.2.2.1

theorem panel22Prefix51_eq :
    P2RoundedFactorCheckpointData.panel22Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk12.2.2.2

end RHP2Bridge
