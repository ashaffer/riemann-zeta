import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk13 :
    P2RoundedFactorCheckpointData.panel22Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix52_eq :
    P2RoundedFactorCheckpointData.panel22Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk13.1

theorem panel22Prefix53_eq :
    P2RoundedFactorCheckpointData.panel22Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk13.2.1

theorem panel22Prefix54_eq :
    P2RoundedFactorCheckpointData.panel22Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk13.2.2.1

theorem panel22Prefix55_eq :
    P2RoundedFactorCheckpointData.panel22Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk13.2.2.2

end RHP2Bridge
