import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk13 :
    P2RoundedFactorCheckpointData.panel2Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix52_eq :
    P2RoundedFactorCheckpointData.panel2Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk13.1

theorem panel2Prefix53_eq :
    P2RoundedFactorCheckpointData.panel2Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk13.2.1

theorem panel2Prefix54_eq :
    P2RoundedFactorCheckpointData.panel2Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk13.2.2.1

theorem panel2Prefix55_eq :
    P2RoundedFactorCheckpointData.panel2Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk13.2.2.2

end RHP2Bridge
