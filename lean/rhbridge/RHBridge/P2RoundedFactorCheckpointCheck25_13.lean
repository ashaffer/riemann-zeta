import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk13 :
    P2RoundedFactorCheckpointData.panel25Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix52_eq :
    P2RoundedFactorCheckpointData.panel25Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk13.1

theorem panel25Prefix53_eq :
    P2RoundedFactorCheckpointData.panel25Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk13.2.1

theorem panel25Prefix54_eq :
    P2RoundedFactorCheckpointData.panel25Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk13.2.2.1

theorem panel25Prefix55_eq :
    P2RoundedFactorCheckpointData.panel25Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk13.2.2.2

end RHP2Bridge
