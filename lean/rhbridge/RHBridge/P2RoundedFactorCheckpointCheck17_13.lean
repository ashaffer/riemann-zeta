import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk13 :
    P2RoundedFactorCheckpointData.panel17Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix52_eq :
    P2RoundedFactorCheckpointData.panel17Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk13.1

theorem panel17Prefix53_eq :
    P2RoundedFactorCheckpointData.panel17Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk13.2.1

theorem panel17Prefix54_eq :
    P2RoundedFactorCheckpointData.panel17Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk13.2.2.1

theorem panel17Prefix55_eq :
    P2RoundedFactorCheckpointData.panel17Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk13.2.2.2

end RHP2Bridge
