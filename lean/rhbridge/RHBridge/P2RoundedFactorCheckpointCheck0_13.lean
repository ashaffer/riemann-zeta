import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk13 :
    P2RoundedFactorCheckpointData.panel0Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix52_eq :
    P2RoundedFactorCheckpointData.panel0Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk13.1

theorem panel0Prefix53_eq :
    P2RoundedFactorCheckpointData.panel0Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk13.2.1

theorem panel0Prefix54_eq :
    P2RoundedFactorCheckpointData.panel0Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk13.2.2.1

theorem panel0Prefix55_eq :
    P2RoundedFactorCheckpointData.panel0Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk13.2.2.2

end RHP2Bridge
