import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk13 :
    P2RoundedFactorCheckpointData.panel10Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix52_eq :
    P2RoundedFactorCheckpointData.panel10Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk13.1

theorem panel10Prefix53_eq :
    P2RoundedFactorCheckpointData.panel10Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk13.2.1

theorem panel10Prefix54_eq :
    P2RoundedFactorCheckpointData.panel10Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk13.2.2.1

theorem panel10Prefix55_eq :
    P2RoundedFactorCheckpointData.panel10Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk13.2.2.2

end RHP2Bridge
