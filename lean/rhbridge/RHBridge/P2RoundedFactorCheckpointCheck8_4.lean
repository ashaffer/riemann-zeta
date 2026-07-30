import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk4 :
    P2RoundedFactorCheckpointData.panel8Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix16_eq :
    P2RoundedFactorCheckpointData.panel8Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk4.1

theorem panel8Prefix17_eq :
    P2RoundedFactorCheckpointData.panel8Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk4.2.1

theorem panel8Prefix18_eq :
    P2RoundedFactorCheckpointData.panel8Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk4.2.2.1

theorem panel8Prefix19_eq :
    P2RoundedFactorCheckpointData.panel8Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk4.2.2.2

end RHP2Bridge
