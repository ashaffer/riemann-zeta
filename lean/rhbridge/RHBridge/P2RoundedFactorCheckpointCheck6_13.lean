import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk13 :
    P2RoundedFactorCheckpointData.panel6Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix52_eq :
    P2RoundedFactorCheckpointData.panel6Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk13.1

theorem panel6Prefix53_eq :
    P2RoundedFactorCheckpointData.panel6Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk13.2.1

theorem panel6Prefix54_eq :
    P2RoundedFactorCheckpointData.panel6Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk13.2.2.1

theorem panel6Prefix55_eq :
    P2RoundedFactorCheckpointData.panel6Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk13.2.2.2

end RHP2Bridge
