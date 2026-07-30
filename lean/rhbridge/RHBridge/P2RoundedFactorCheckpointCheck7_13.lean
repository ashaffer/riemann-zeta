import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk13 :
    P2RoundedFactorCheckpointData.panel7Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix52_eq :
    P2RoundedFactorCheckpointData.panel7Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk13.1

theorem panel7Prefix53_eq :
    P2RoundedFactorCheckpointData.panel7Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk13.2.1

theorem panel7Prefix54_eq :
    P2RoundedFactorCheckpointData.panel7Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk13.2.2.1

theorem panel7Prefix55_eq :
    P2RoundedFactorCheckpointData.panel7Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk13.2.2.2

end RHP2Bridge
