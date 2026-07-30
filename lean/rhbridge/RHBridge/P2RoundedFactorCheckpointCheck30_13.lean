import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk13 :
    P2RoundedFactorCheckpointData.panel30Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix52_eq :
    P2RoundedFactorCheckpointData.panel30Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk13.1

theorem panel30Prefix53_eq :
    P2RoundedFactorCheckpointData.panel30Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk13.2.1

theorem panel30Prefix54_eq :
    P2RoundedFactorCheckpointData.panel30Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk13.2.2.1

theorem panel30Prefix55_eq :
    P2RoundedFactorCheckpointData.panel30Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk13.2.2.2

end RHP2Bridge
