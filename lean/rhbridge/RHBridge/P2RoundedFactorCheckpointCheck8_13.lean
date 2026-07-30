import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk13 :
    P2RoundedFactorCheckpointData.panel8Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix52_eq :
    P2RoundedFactorCheckpointData.panel8Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk13.1

theorem panel8Prefix53_eq :
    P2RoundedFactorCheckpointData.panel8Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk13.2.1

theorem panel8Prefix54_eq :
    P2RoundedFactorCheckpointData.panel8Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk13.2.2.1

theorem panel8Prefix55_eq :
    P2RoundedFactorCheckpointData.panel8Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk13.2.2.2

end RHP2Bridge
