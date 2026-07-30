import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk13 :
    P2RoundedFactorCheckpointData.panel4Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix52_eq :
    P2RoundedFactorCheckpointData.panel4Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk13.1

theorem panel4Prefix53_eq :
    P2RoundedFactorCheckpointData.panel4Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk13.2.1

theorem panel4Prefix54_eq :
    P2RoundedFactorCheckpointData.panel4Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk13.2.2.1

theorem panel4Prefix55_eq :
    P2RoundedFactorCheckpointData.panel4Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk13.2.2.2

end RHP2Bridge
